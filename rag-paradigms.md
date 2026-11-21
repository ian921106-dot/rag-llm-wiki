---
title: RAG 的三種典範：Naive / Advanced / Modular
type: concept
sources: [S2]
---
# RAG 的三種典範 [S2]

## 1. Naive RAG（樸素 RAG）
「Retrieve-Read」：建索引 → 檢索 → 生成。
缺點：檢索精確率與召回率差、可能幻覺、回答零散重複、單次檢索對複雜問題不夠。

## 2. Advanced RAG（進階 RAG）
- **檢索前**：更細的資料粒度、滑動視窗、metadata、混合檢索（[[concepts/bm25-hybrid-search]]）、查詢改寫或擴展
- **檢索後**：rerank（[[concepts/reranking-topk]]）、壓縮或篩選 context

## 3. Modular RAG（模組化 RAG）
把搜尋、記憶、路由等做成可重組的模組；支援迭代、遞迴、自適應檢索，也可結合微調。

## 比喻
Naive = 查一次就寫；Advanced = 查之前先想好關鍵字、查完再挑重點；Modular = 一個會自己決定要不要再查、去哪查的研究助理。

相關：[[concepts/what-is-rag]]、[[sources/S2]]
