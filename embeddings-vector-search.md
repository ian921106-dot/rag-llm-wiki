---
title: Embedding 與向量搜尋
type: concept
sources: [S1, S2, S3]
---
# Embedding 與向量搜尋

- **Embedding**：把一段文字轉成一串數字（向量），意思相近的文字，向量也會靠近 [S2][S3]。
- **向量資料庫**：存放所有 chunk 的向量 [S2][S3]。
- **向量搜尋**：把問題也轉成向量，找出相似度最高的 top K 個 chunk [S2]。
- 原始 RAG 論文用的檢索器是 DPR（Dense Passage Retriever），索引是 Wikipedia 的稠密向量索引 [S1]。

## 比喻
像在圖書館用「意思」找書，而不是用書名一字不差地查。

## 弱點
語意相近不等於字詞精確吻合；遇到專有名詞、代碼、型號時，可以加上關鍵字搜尋 → [[concepts/bm25-hybrid-search]]

相關：[[concepts/indexing-chunking]]、[[concepts/reranking-topk]]
