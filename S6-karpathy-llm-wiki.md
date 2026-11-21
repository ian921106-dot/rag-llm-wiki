---
id: S6
title: LLM Wiki
authors: Andrej Karpathy
venue: GitHub gist, 2026-04
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
ingested: 2026-11-22
---
# 原始重點（ingest 時擷取，之後不修改）
- 一種用 LLM 建立個人知識庫的模式。
- 和一般 RAG 不同：RAG 在每次查詢時從原始文件重新找、重新推導；LLM Wiki 則由 LLM 逐步建立並維護一個持久的、互相連結的 markdown wiki，放在使用者與原始資料之間。
- 三層：raw sources（不可改）、wiki、schema（規則檔）。
- 三個操作：ingest（一次一篇，一篇來源可能更新 10–15 頁）、query（對 wiki 提問，好的答案可回寫）、lint（定期健康檢查：孤兒頁、壞連結、矛盾、過時說法）。
- index.md 是內容目錄，log.md 是時間順序紀錄。
- 知識在 ingest 時整理一次並持續更新，而不是每次查詢都重算。
