---
id: S3
title: Introducing Contextual Retrieval
authors: Anthropic
venue: Anthropic Engineering blog, 2024-09
url: https://www.anthropic.com/news/contextual-retrieval
ingested: 2026-11-22
---
# 原始重點（ingest 時擷取，之後不修改）
- 標準 RAG：把語料切成 chunk（通常幾百個 token）→ 轉 embedding 存入向量資料庫 → 查詢時取語意最相近的 top-K 放進 prompt。
- 混合版：同時跑 BM25（以 TF-IDF 為基礎的精確詞比對），用 rank fusion 合併結果。
- 問題：切 chunk 會讓片段失去上下文；例如一段寫營收「成長 3%」，卻沒寫是哪家公司、哪一季。
- Contextual Retrieval：在建 embedding 與 BM25 索引前，用 Claude 根據整份文件替每個 chunk 加上 50–100 token 的說明前綴。
- 結果（top-20 檢索失敗率，基準 5.7%）：Contextual Embeddings 3.7%（降 35%）；再加 Contextual BM25 2.9%（降 49%）；再加 reranking 1.9%（降 67%）。
- 傳 20 個 chunk 比傳 5 或 10 個表現更好。
- Reranking：先取約 150 個候選，用 reranker 評分後留下 top 20；會多一點延遲。
- 知識庫小於 200,000 token（約 500 頁）時，可以不用 RAG，直接全部放進 prompt；prompt caching 可讓延遲降低超過 2 倍、成本最多省 90%。
