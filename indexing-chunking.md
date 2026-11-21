---
title: 建索引與切塊（Indexing & Chunking）
type: concept
sources: [S2, S3]
---
# 建索引與切塊（Indexing & Chunking）

## 流程
原始文件 → 清理 → **切成 chunk** → 轉成向量 → 存入向量資料庫 [S2]

- chunk 通常是幾百個 token 的片段 [S3]。
- 為什麼要切：整份文件太大，切小比較好檢索。

## 切塊的副作用：失去上下文
例子：某段寫「營收比上一季成長 3%」，但這段本身沒寫是哪家公司、哪一季，所以很難被找到，也很難被正確使用 [S3]。
→ 解法之一：[[concepts/contextual-retrieval]]

## Advanced RAG 的切塊改良
更細的資料粒度、滑動視窗（sliding window）、加上 metadata [S2]。見 [[concepts/rag-paradigms]]。

相關：[[concepts/embeddings-vector-search]]、[[concepts/what-is-rag]]
