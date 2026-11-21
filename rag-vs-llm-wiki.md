---
title: RAG vs LLM Wiki
type: concept
sources: [S6]
---
# RAG vs LLM Wiki

| | 傳統 RAG | LLM Wiki |
|---|---|---|
| 知識何時整理 | 每次查詢時從原始文件重新找 | ingest 時整理一次，之後持續維護 [S6] |
| 中間層 | 沒有，直接檢索 raw chunk | LLM 寫好的、互相連結的 markdown 頁面 [S6] |
| 維護 | 重建索引 | ingest / query / lint 三個操作 [S6] |

## 本 Wiki 就是一個例子
這個 RAG LLM Wiki 本身就用 LLM Wiki 的方式建立，教學簡報也只用它當知識來源：raw/ 存來源筆記，wiki/ 是整理後的頁面，SCHEMA.md 是規則，tools/check.py 負責 lint。

相關：[[concepts/what-is-rag]]、[[sources/S6]]
