#!/usr/bin/env python3
"""RAG LLM Wiki 檢查器（lint + 簡報出處檢查）

用法：
  python3 check.py wiki   <wiki_root>                 # 檢查 Wiki 本身
  python3 check.py slides <wiki_root> <slides.html>   # 檢查簡報是否都出自 Wiki
回傳碼 0 = 全部通過，1 = 有錯誤（loop 需要回到上一個節點修正）
"""
import re, sys, json, pathlib
from html.parser import HTMLParser

LINK = re.compile(r"\[\[([^\]]+)\]\]")
CITE = re.compile(r"\[(S\d+)\]")
NUM = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*%?(?![\w])")
URL = re.compile(r"https?://\S+")
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)


def numbers(text):
    text = URL.sub(" ", text)
    text = LINK.sub(" ", text)
    text = CITE.sub(" ", text)
    text = re.sub(r"\bS\d+\b", " ", text)
    text = re.sub(r"^\s*(?:#+\s*)?\d+\.\s", " ", text, flags=re.M)  # 編號清單與編號標題 1. 2. 3.
    out = set()
    for m in NUM.finditer(text):
        n = m.group(0).rstrip("%").replace(",", "")
        out.add(n)
    return out


def load_wiki(root):
    root = pathlib.Path(root)
    pages = {}
    for p in list((root / "wiki").rglob("*.md")) + [root / "index.md"]:
        key = "index" if p.name == "index.md" and p.parent == root else str(p.relative_to(root / "wiki"))[:-3]
        raw = p.read_text(encoding="utf-8")
        m = FM.match(raw)
        fm, body = (m.group(1), raw[m.end():]) if m else ("", raw)
        srcs = re.findall(r"S\d+", re.search(r"sources:\s*\[(.*?)\]", fm).group(1)) if "sources:" in fm else []
        pages[key] = {"body": body, "sources": srcs}
    raws = {}
    for p in (root / "raw").glob("S*.md"):
        raws[p.name.split("-")[0]] = p.read_text(encoding="utf-8")
    return pages, raws


def raw_numbers(raws, ids):
    s = set()
    for i in ids:
        s |= numbers(raws.get(i, "")) | {n.replace(",", "") for n in re.findall(r"\d[\d,]*(?:\.\d+)?", raws.get(i, ""))}
    return s


def check_wiki(root):
    pages, raws = load_wiki(root)
    errors = []
    inbound = {k: 0 for k in pages}
    for k, pg in pages.items():
        for link in LINK.findall(pg["body"]):
            if link not in pages:
                errors.append({"rule": "W1 壞連結", "page": k, "detail": f"[[{link}]] 不存在"})
            elif link != k:
                inbound[link] += 1
        if k != "index" and not pg["sources"]:
            errors.append({"rule": "W4 無出處", "page": k, "detail": "frontmatter 沒有 sources"})
        for s in pg["sources"]:
            if s not in raws:
                errors.append({"rule": "W4 無出處", "page": k, "detail": f"{s} 沒有對應的 raw 筆記"})
        for c in set(CITE.findall(pg["body"])):
            if c not in pg["sources"]:
                errors.append({"rule": "W6 引用不一致", "page": k, "detail": f"內文引用 [{c}] 但 frontmatter 沒列"})
        allowed = raw_numbers(raws, pg["sources"])
        for n in sorted(numbers(pg["body"])):
            if n not in allowed:
                errors.append({"rule": "W5 數字無出處", "page": k, "detail": f"數字「{n}」在 {pg['sources']} 的 raw 筆記裡找不到"})
    for k, pg in pages.items():
        if k.startswith("sources/"):
            if not re.search(r"\b(19|20)\d{2}\b", re.sub(r"raw/\S+", " ", URL.sub(" ", pg["body"]))):
                errors.append({"rule": "W7 來源頁缺年份", "page": k, "detail": "來源摘要頁沒有寫出版年份（簡報引用時會用到）"})
            if not URL.search(pg["body"]):
                errors.append({"rule": "W7 來源頁缺網址", "page": k, "detail": "來源摘要頁沒有網址"})
    index_links = set(LINK.findall(pages["index"]["body"]))
    for k in pages:
        if k == "index":
            continue
        if inbound[k] == 0:
            errors.append({"rule": "W2 孤兒頁", "page": k, "detail": "沒有任何頁面連到這裡"})
        if k not in index_links:
            errors.append({"rule": "W3 目錄漏列", "page": k, "detail": "index.md 沒有列出"})
    return {"target": "wiki", "pages": len(pages), "sources": len(raws), "errors": errors}


class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides, self.cur, self.depth = [], None, 0
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and "slide" in (a.get("class") or ""):
            self.cur = {"id": a.get("id"), "wiki": (a.get("data-wiki") or "").split(), "text": "", "has_src": False}
            self.depth = 1
            return
        if self.cur is not None:
            if tag == "section":
                self.depth += 1
            if "src-note" in (a.get("class") or ""):
                self.cur["has_src"] = True
            if tag in ("script", "style"):
                self.skip += 1

    def handle_endtag(self, tag):
        if self.cur is not None:
            if tag in ("script", "style"):
                self.skip -= 1
            if tag == "section":
                self.depth -= 1
                if self.depth == 0:
                    self.slides.append(self.cur)
                    self.cur = None

    def handle_data(self, data):
        if self.cur is not None and not self.skip:
            self.cur["text"] += data + " | "


TERM = re.compile(r"\b[A-Z][A-Za-z0-9\-]{1,}(?:\s[A-Z][A-Za-z\-]+)*\b")
TERM_ALLOW = {"Wiki", "LLM", "AI", "Q", "A", "OK", "Step", "Claude"}


def check_slides(root, html_path):
    pages, raws = load_wiki(root)
    p = SlideParser()
    p.feed(pathlib.Path(html_path).read_text(encoding="utf-8"))
    errors = []
    used = set()
    for i, s in enumerate(p.slides, 1):
        sid = s["id"] or f"slide-{i}"
        if not s["wiki"]:
            errors.append({"rule": "P1 沒標 Wiki 來源", "page": sid, "detail": "section 缺 data-wiki"})
            continue
        bad = [w for w in s["wiki"] if w not in pages]
        for w in bad:
            errors.append({"rule": "P1 Wiki 頁不存在", "page": sid, "detail": w})
        refs = [w for w in s["wiki"] if w in pages]
        used |= set(refs)
        for c in sorted(set(CITE.findall(s["text"]))):
            if f"sources/{c}" in pages and f"sources/{c}" not in refs:
                refs.append(f"sources/{c}")
        corpus = " ".join(pages[w]["body"] for w in refs)
        allowed = numbers(corpus) | {n.replace(",", "") for n in re.findall(r"\d[\d,]*(?:\.\d+)?", corpus)}
        text_nokicker = re.sub(r"\b\d{2}\s*·", " ", s["text"])
        for n in sorted(numbers(text_nokicker)):
            if n not in allowed:
                errors.append({"rule": "P2 數字不在 Wiki", "page": sid, "detail": f"「{n}」不在 {refs}"})
        low = corpus.lower()
        for t in sorted(set(TERM.findall(s["text"]))):
            if t in TERM_ALLOW or len(t) < 3:
                continue
            if t.lower() not in low:
                errors.append({"rule": "P3 術語不在 Wiki", "page": sid, "detail": f"「{t}」不在 {refs}"})
        if not s["has_src"]:
            errors.append({"rule": "P4 缺出處標示", "page": sid, "detail": "投影片上沒有 .src-note"})
    core = [l for l in LINK.findall(pages["index"]["body"]) if l.startswith("concepts/")]
    for c in core:
        if c not in used:
            errors.append({"rule": "P5 覆蓋率", "page": c, "detail": "這個 Wiki 概念沒有出現在簡報"})
    return {"target": "slides", "slides": len(p.slides), "errors": errors}


if __name__ == "__main__":
    mode = sys.argv[1]
    res = check_wiki(sys.argv[2]) if mode == "wiki" else check_slides(sys.argv[2], sys.argv[3])
    print(json.dumps(res, ensure_ascii=False, indent=1))
    sys.exit(1 if res["errors"] else 0)
