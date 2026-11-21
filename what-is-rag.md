---
title: RAG 是什麼？
type: overview
sources: [S1, S2, S3]
---
# RAG 是什麼？（Retrieval-Augmented Generation，檢索增強生成）

**一句話**：先「查資料」，再「寫答案」。模型回答前，先從外部知識庫找出相關片段，把片段和問題一起放進 prompt，讓模型根據這些資料生成答案 [S2][S3]。

## 為什麼需要它
大型語言模型把知識存在參數裡，但會有幻覺、知識過時、答案不透明不可追溯的問題 [S2]。詳見 [[concepts/hallucination-and-limits]]。

## 起源
2020 年 Lewis 等人提出 RAG：把預訓練的生成模型（參數式記憶）接上一個可檢索的 Wikipedia 向量索引（非參數式記憶），在三個開放領域問答任務達到 state-of-the-art [S1]。見 [[concepts/parametric-vs-nonparametric]]、[[sources/S1]]。

## 三個步驟（Naive RAG）
1. **Indexing 建索引**：切 chunk、轉向量、存資料庫 → [[concepts/indexing-chunking]]、[[concepts/embeddings-vector-search]]
2. **Retrieval 檢索**：把問題轉向量，找最相似的 top K 個 chunk → [[concepts/reranking-topk]]
3. **Generation 生成**：問題 + chunk 組成 prompt 交給 LLM [S2]

## 生活比喻
閉卷考試 vs 開書考試：一般 LLM 像閉卷，只能靠記憶；RAG 像開書考，先翻到對的頁再作答。翻錯頁（檢索失敗），答案一樣會錯。

## 延伸
- 進階做法：[[concepts/rag-paradigms]]、[[concepts/contextual-retrieval]]、[[concepts/bm25-hybrid-search]]
- 什麼時候不用 RAG：[[concepts/rag-vs-finetuning-vs-long-context]]
- 怎麼評估：[[concepts/rag-evaluation]]
- 和 LLM Wiki 的差別：[[concepts/rag-vs-llm-wiki]]
