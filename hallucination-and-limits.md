---
title: LLM 的限制：幻覺、知識過時、不可追溯
type: concept
sources: [S1, S2]
---
# LLM 的限制：為什麼需要 RAG

1. **幻覺（hallucination）**：模型自信地說出不正確的內容，尤其是問題超出訓練資料或需要最新資訊時 [S2]。
2. **知識過時**：知識凍結在訓練時；更新要重新訓練 [S1][S2]。
3. **不透明、不可追溯**：看不出答案依據什麼 [S2]；提供出處（provenance）是 RAG 論文想解決的問題之一 [S1]。

## RAG 怎麼幫忙
- 回答時附上檢索到的資料 → 可以檢查依據
- 換掉知識庫就能更新知識 → 不用重新訓練 [S1]

## 但 RAG 不是萬靈丹
- 檢索錯了，答案照樣錯：Naive RAG 的檢索精確率與召回率不佳，仍可能幻覺 [S2]
- 放進太多資料，模型可能忽略中間段落 → [[concepts/lost-in-the-middle]]

相關：[[concepts/what-is-rag]]、[[concepts/parametric-vs-nonparametric]]
