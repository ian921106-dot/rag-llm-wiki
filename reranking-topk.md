---
title: Top-K 與重排序（Reranking）
type: concept
sources: [S2, S3, S4]
---
# Top-K 與重排序

## Top-K
檢索後只把最相似的 K 個 chunk 放進 prompt [S2]。在 Anthropic 的實驗中，傳 20 個 chunk 比傳 5 或 10 個表現更好 [S3]。

## Reranking（重排序）
1. 先粗撈較多候選（實驗中約 150 個）
2. 用 reranker 模型逐一評分
3. 只留下最好的 20 個 [S3]

代價：多一點延遲 [S3]。

## 放的位置也很重要
Advanced RAG 會把最相關的 chunk 放在 prompt 的兩端 [S2]，因為模型容易忽略中間的資訊 → [[concepts/lost-in-the-middle]] [S4]。

相關：[[concepts/contextual-retrieval]]、[[concepts/rag-paradigms]]
