---
title: BM25 與混合檢索（Hybrid Search）
type: concept
sources: [S2, S3]
---
# BM25 與混合檢索

- **BM25**：以 TF-IDF（詞頻–逆文件頻率）為基礎的排序方法，擅長**精確字詞比對** [S3]。
- **混合檢索**：同時做向量搜尋（語意）與 BM25（關鍵字），再用 rank fusion 合併排名 [S3]。混合檢索也被列為 Advanced RAG 的檢索前改良之一 [S2]。

## 什麼時候特別有用
問題裡有專有名詞或編號時，語意搜尋可能抓不準，BM25 可以補上。

相關：[[concepts/embeddings-vector-search]]、[[concepts/contextual-retrieval]]、[[concepts/rag-paradigms]]
