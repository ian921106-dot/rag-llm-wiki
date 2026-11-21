---
id: S5
title: Ragas: Automated Evaluation of Retrieval Augmented Generation
authors: Shahul Es et al.
venue: arXiv 2309.15217 (2023), EACL 2024 demo
url: https://arxiv.org/abs/2309.15217
ingested: 2026-11-22
---
# 原始重點（ingest 時擷取，之後不修改）
- Ragas 是 RAG 流程的「免參考答案」（reference-free）自動評估框架。
- 三個核心品質面向：
  - Faithfulness（忠實度）：答案應該以給定的 context 為根據。
  - Answer Relevance（答案相關性）：答案應該回應實際被問的問題。
  - Context Relevance（context 相關性）：檢索到的 context 應該聚焦，盡量少不相關的內容。
- 後續版本的工具常用四個指標：faithfulness、answer relevancy（診斷生成器），context precision、context recall（診斷檢索器）。
