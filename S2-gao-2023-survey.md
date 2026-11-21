---
id: S2
title: Retrieval-Augmented Generation for Large Language Models: A Survey
authors: Yunfan Gao et al. (Tongji University, Fudan University)
venue: arXiv 2312.10997 (v1 2023-12, v5 2024-03)
url: https://arxiv.org/abs/2312.10997
ingested: 2026-11-22
---
# 原始重點（ingest 時擷取，之後不修改）
- LLM 的挑戰：幻覺、知識過時、推理過程不透明不可追溯；RAG 透過引入外部資料庫知識來解決。
- 三種典範：Naive RAG、Advanced RAG、Modular RAG。
- Naive RAG = 「Retrieve-Read」：Indexing（清理、切 chunk、轉向量、存向量資料庫）→ Retrieval（問題轉向量、比相似度、取 top K）→ Generation（問題 + chunk 組成 prompt 給 LLM）。
- Naive RAG 缺點：檢索精確率與召回率差、幻覺或偏差、回答零散重複、單次檢索對複雜問題不夠。
- Advanced RAG：檢索前（更細的資料粒度、滑動視窗、metadata、混合檢索、查詢改寫/擴展）；檢索後（rerank 把最相關的放在 prompt 兩端、壓縮或篩選 context）。
- Modular RAG：可重組的模組（搜尋、記憶、路由等），支援迭代、遞迴、自適應檢索。
- RAG vs 微調：RAG 可即時更新知識、可解釋性高但增加延遲；微調較靜態、更新要重新訓練、可深度客製行為風格但運算昂貴；兩者可並用。
- 評估：檢索品質（Hit Rate、MRR、NDCG）與生成品質；三個品質分數：context relevance、answer faithfulness、answer relevance；四種能力：noise robustness、negative rejection、information integration、counterfactual robustness。
