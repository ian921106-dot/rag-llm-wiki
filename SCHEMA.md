# SCHEMA — RAG LLM Wiki 的維護規則

這份檔案是 LLM（維護者）的操作手冊，參考 Karpathy 的 LLM Wiki 模式：
**raw（原始資料，不可改）→ wiki（LLM 整理的頁面）→ schema（本檔，規則）**。

## 三種操作
1. **Ingest**：一次處理一篇來源。先在 `raw/` 建立來源筆記（網址、作者、年份、重點），
   再更新或新增 `wiki/sources/` 的來源摘要頁與 `wiki/concepts/` 的概念頁，最後更新 `index.md` 與 `log.md`。
2. **Query**：回答問題或產生簡報時，**只能讀 `index.md` → 相關 wiki 頁面**，不可直接憑記憶補內容。
   有價值的新整理可回寫成新頁面。
3. **Lint**：健康檢查（`tools/check.py`）——壞連結、孤兒頁、沒有出處的頁面、index 漏列、數字無出處。

## 頁面格式
- 每頁開頭有 frontmatter：`title`、`type`（concept / source / overview）、`sources`（如 `[S1, S3]`）。
- 內文的事實句後面標出處 `[S1]`；數字一定要有出處。
- 頁面之間用 `[[concepts/xxx]]` 互相連結。
- 用繁體中文寫，專有名詞第一次出現附英文。

## 來源代號
| 代號 | 來源 |
|---|---|
| S1 | Lewis et al., 2020, *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (NeurIPS) |
| S2 | Gao et al., 2023/2024, *Retrieval-Augmented Generation for Large Language Models: A Survey* |
| S3 | Anthropic, 2024, *Introducing Contextual Retrieval* |
| S4 | Liu et al., 2023/2024, *Lost in the Middle: How Language Models Use Long Contexts* (TACL) |
| S5 | Es et al., 2023, *Ragas: Automated Evaluation of Retrieval Augmented Generation* |
| S6 | Karpathy, 2026, *LLM Wiki*（GitHub gist） |
