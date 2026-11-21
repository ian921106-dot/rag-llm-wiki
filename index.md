---
title: RAG LLM Wiki — 目錄
type: overview
sources: [S1, S2, S3, S4, S5, S6]
---
# RAG LLM Wiki — 目錄

主題：**RAG（Retrieval-Augmented Generation，檢索增強生成）**。
讀者：沒學過 RAG 的人。建議閱讀順序由上而下。

## 入門
- [[concepts/what-is-rag]] — 一句話、三步驟、開書考比喻
- [[concepts/hallucination-and-limits]] — 為什麼 LLM 需要 RAG
- [[concepts/parametric-vs-nonparametric]] — 兩種記憶

## RAG 怎麼運作
- [[concepts/indexing-chunking]] — 切塊與建索引
- [[concepts/embeddings-vector-search]] — 用「意思」找資料
- [[concepts/bm25-hybrid-search]] — 加上關鍵字搜尋
- [[concepts/reranking-topk]] — 挑出最好的幾段

## 進階
- [[concepts/contextual-retrieval]] — 替 chunk 補上下文
- [[concepts/lost-in-the-middle]] — 塞太多反而忽略中間
- [[concepts/rag-paradigms]] — Naive / Advanced / Modular

## 選擇與評估
- [[concepts/rag-vs-finetuning-vs-long-context]] — 什麼時候用 RAG
- [[concepts/rag-evaluation]] — 怎麼知道 RAG 做得好不好
- [[concepts/rag-vs-llm-wiki]] — RAG 和本 Wiki 的做法有什麼不同

## 來源（6 篇）
- [[sources/S1]] Lewis et al. 2020 — RAG 原始論文
- [[sources/S2]] Gao et al. — RAG 綜述
- [[sources/S3]] Anthropic — Contextual Retrieval
- [[sources/S4]] Liu et al. — Lost in the Middle
- [[sources/S5]] Es et al. — Ragas
- [[sources/S6]] Karpathy — LLM Wiki
