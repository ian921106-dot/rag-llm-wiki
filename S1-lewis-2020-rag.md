---
id: S1
title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
authors: Patrick Lewis et al. (Facebook AI Research, UCL, NYU)
venue: NeurIPS 2020
url: https://arxiv.org/abs/2005.11401
ingested: 2026-11-22
---
# 原始重點（ingest 時擷取，之後不修改）
- 預訓練語言模型把事實知識存在參數裡，但在知識密集任務上，精準存取與操作知識的能力有限；提供決策出處（provenance）與更新世界知識仍是未解問題。
- 純參數模型的缺點：不易擴充或修正記憶、難以解釋預測、可能產生幻覺（hallucination）。
- 提出 RAG：結合「參數式記憶」（預訓練 seq2seq 模型，BART）與「非參數式記憶」（Wikipedia 的稠密向量索引），用預訓練的神經檢索器（DPR）存取。
- 兩種形式：整段輸出共用同一批檢索段落（RAG-Sequence），或每個 token 可用不同段落（RAG-Token）。
- 在三個開放領域問答任務達到 state-of-the-art。
- 非參數記憶可以被替換，藉此更新模型所用的知識，而不必重新訓練。
