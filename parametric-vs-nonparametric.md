---
title: 參數式記憶 vs 非參數式記憶
type: concept
sources: [S1]
---
# 參數式記憶 vs 非參數式記憶

| | 參數式記憶（parametric） | 非參數式記憶（non-parametric） |
|---|---|---|
| 存在哪 | 模型權重裡 | 外部文件索引（如 Wikipedia 向量索引） |
| RAG 論文中的元件 | 預訓練 seq2seq 模型 BART | 稠密向量索引，用 DPR 檢索器存取 |
| 更新知識 | 要重新訓練 | 直接替換索引即可 |
| 可解釋性 | 難以看出依據 | 可以檢視檢索到的內容 |

來源：[S1]

## 重點
- 純參數模型不易擴充或修正記憶，也難以解釋預測，還可能產生幻覺 [S1]。
- RAG 把兩種記憶結合：檢索器提供文件，生成器根據文件與輸入一起生成 [S1]。
- 論文示範：把非參數記憶換掉，就能更新模型使用的知識 [S1]。

相關：[[concepts/what-is-rag]]、[[concepts/hallucination-and-limits]]、[[sources/S1]]
