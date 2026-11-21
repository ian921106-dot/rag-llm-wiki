---
title: Lost in the Middle（迷失在中間）
type: concept
sources: [S2, S4]
---
# Lost in the Middle

## 發現
研究者用多文件問答和 key-value 檢索測試語言模型：相關資訊放在**開頭或結尾**時表現最好，放在**中間**時表現明顯下降，連長上下文模型也一樣；輸入越長，表現也越差 [S4]。

## 對 RAG 的意義
- 不是塞越多 chunk 越好
- 最相關的資料應該放在 prompt 兩端 [S2]
- 可以先 rerank、壓縮或篩選 context，減少資訊過載 [S2]

相關：[[concepts/reranking-topk]]、[[concepts/rag-vs-finetuning-vs-long-context]]、[[sources/S4]]
