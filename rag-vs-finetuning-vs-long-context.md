---
title: RAG vs 微調 vs 長上下文
type: concept
sources: [S2, S3, S4]
---
# 什麼時候用 RAG？

| 方法 | 優點 | 缺點 |
|---|---|---|
| **RAG** | 知識可即時更新、可解釋性高 [S2] | 多一步檢索，增加延遲 [S2] |
| **微調（Fine-tuning）** | 可深度客製模型的行為與風格 [S2] | 較靜態，更新知識要重新訓練，運算昂貴 [S2] |
| **長上下文（整包放進 prompt）** | 最簡單，不用建檢索系統 [S3] | 只適合小知識庫；長輸入中間的資訊容易被忽略 [S4] |

- RAG 和微調不互斥，可以一起用 [S2]。
- 知識庫小於 200,000 token（約 500 頁）時，可考慮直接整包放進 prompt；搭配 prompt caching，延遲可降低超過 2 倍、成本最多省 90% [S3]。

相關：[[concepts/what-is-rag]]、[[concepts/lost-in-the-middle]]
