#!/usr/bin/env python3
"""把 rag-wiki/ 的 markdown 轉成一個可瀏覽的單頁 HTML Wiki。"""
import re, json, html, pathlib, sys, markdown

root = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); checker = pathlib.Path(sys.argv[3])
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)

def slug(key): return re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")

entries = []  # (group, key, title, md)
def add(group, key, path):
    raw = path.read_text(encoding="utf-8")
    m = FM.match(raw); fm = m.group(1) if m else ""; body = raw[m.end():] if m else raw
    t = re.search(r"^title:\s*\"?(.*?)\"?$", fm, re.M)
    title = t.group(1) if t else path.stem
    if group == "原始資料 raw":
        body = "```yaml\n" + fm + "\n```\n" + body
    entries.append((group, key, title, body))

add("首頁", "index", root / "index.md")
order = ["what-is-rag","hallucination-and-limits","parametric-vs-nonparametric","indexing-chunking",
         "embeddings-vector-search","bm25-hybrid-search","reranking-topk","contextual-retrieval",
         "lost-in-the-middle","rag-paradigms","rag-vs-finetuning-vs-long-context","rag-evaluation","rag-vs-llm-wiki"]
for o in order: add("概念 concepts", f"concepts/{o}", root / "wiki/concepts" / f"{o}.md")
for i in range(1, 7): add("來源摘要 sources", f"sources/S{i}", root / "wiki/sources" / f"S{i}.md")
for p in sorted((root / "raw").glob("S*.md")): add("原始資料 raw", f"raw/{p.stem}", p)
add("維護", "schema", root / "SCHEMA.md")
add("維護", "log", root / "log.md")
entries.append(("維護", "checker", "檢查器 tools/check.py", "以下是 lint 與簡報出處檢查用的腳本（v2）。\n\n```python\n" + checker.read_text(encoding="utf-8") + "\n```\n"))

keys = {e[1] for e in entries}
pages = {}
for group, key, title, body in entries:
    def link(m):
        k = m.group(1)
        lbl = next((e[2] for e in entries if e[1] == k), k)
        cls = "wl" if k in keys else "wl broken"
        return f'<a class="{cls}" href="#{slug(k)}">{html.escape(lbl)}</a>'
    parts = re.split(r"(```.*?```|`[^`\n]*`)", body, flags=re.S)
    for j in range(0, len(parts), 2):
        parts[j] = re.sub(r"\[\[([^\]]+)\]\]", lambda m: "\x00L" + m.group(1) + "\x00", parts[j])
    b = "".join(parts)
    b = re.sub(r"(?<!\[)\[(S\d)\](?!\])", lambda m: f"\x00C{m.group(1)}\x00", b)
    h = markdown.markdown(b, extensions=["tables", "fenced_code"])
    h = re.sub(r"\x00L(.*?)\x00", link, h)
    h = re.sub(r"\x00C(S\d)\x00", lambda m: f'<a class="cite" href="#{slug("sources/"+m.group(1))}">{m.group(1)}</a>', h)
    pages[slug(key)] = {"g": group, "t": title, "h": h, "k": key}

nav = {}
for s, p in pages.items(): nav.setdefault(p["g"], []).append((s, p["t"]))
nav_html = ""
for g, items in nav.items():
    nav_html += f'<div class="ng">{html.escape(g)}</div>' + "".join(
        f'<a class="nl" data-s="{s}" href="#{s}">{html.escape(t)}</a>' for s, t in items)

tpl = (pathlib.Path(__file__).parent / "wiki_template.html").read_text(encoding="utf-8")
out.write_text(tpl.replace("/*PAGES*/", json.dumps(pages, ensure_ascii=False).replace("</", "<\\/"))
               .replace("<!--NAV-->", nav_html), encoding="utf-8")
print("pages:", len(pages))
