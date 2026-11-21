---
title: 怎麼評估 RAG？
type: concept
sources: [S2, S5]
---
# 怎麼評估 RAG？

## 兩個要評估的對象 [S2]
- **檢索品質**：Hit Rate、MRR、NDCG
- **生成品質**：忠實、相關、無害；有標準答案時看正確率

## 三個核心分數（RAG Triad）[S2][S5]
| 指標 | 問的問題 | 診斷誰 |
|---|---|---|
| Context Relevance | 找回來的資料是否聚焦、少雜訊？ | 檢索器 |
| Faithfulness | 答案是否只根據找回來的資料？ | 生成器 |
| Answer Relevance | 答案有沒有回答到問題？ | 生成器 |

Ragas 是一個不需要參考答案（reference-free）的自動評估框架 [S5]。

## 四種該具備的能力 [S2]
- Noise robustness：資料有雜訊也不被帶偏
- Negative rejection：資料裡沒有答案時要拒答
- Information integration：整合多份文件
- Counterfactual robustness：能忽略資料中的錯誤資訊

相關：[[concepts/what-is-rag]]、[[sources/S5]]
