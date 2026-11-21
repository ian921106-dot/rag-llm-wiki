---
title: Contextual Retrieval（情境化檢索）
type: concept
sources: [S3]
---
# Contextual Retrieval（情境化檢索）

## 要解決的問題
切 chunk 後，片段失去上下文（「成長 3%」——誰？哪一季？）[S3]。見 [[concepts/indexing-chunking]]。

## 做法
建索引前，讓 LLM 讀整份文件，替每個 chunk 寫一段 50–100 token 的說明前綴，再拿「前綴 + chunk」去做 embedding 和 BM25 索引 [S3]。

## 實驗數字（top-20 檢索失敗率）[S3]
| 方法 | 失敗率 | 相對基準降低 |
|---|---|---|
| 基準（一般 embedding + BM25） | 5.7% | — |
| Contextual Embeddings | 3.7% | 35% |
| + Contextual BM25 | 2.9% | 49% |
| + Reranking | 1.9% | 67% |

## 注意
這些數字來自 Anthropic 自己的部落格實驗，屬於廠商發表的結果。

相關：[[concepts/bm25-hybrid-search]]、[[concepts/reranking-topk]]、[[sources/S3]]
