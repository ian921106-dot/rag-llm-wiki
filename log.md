---
title: 維護紀錄（log）
type: overview
sources: []
---
# 維護紀錄（時間順序，Asia/Taipei）

## 2026-11-22 00:03 — 討論（先討論、後生成）
- 主題候選：AI Agents / RAG / Prompt Engineering → **選定 RAG**（和 LLM Wiki 概念相近，適合教學）。
- 資料來源：由 LLM 上網找，標準＝原始論文、綜述、官方技術文章、評估方法、反面發現，各至少一篇。
- 交付形式：Wiki 與 HTML 簡報都發佈成可分享連結。
- 讀者設定：完全沒學過 RAG 的人 → 每頁要有比喻、少公式。

## 2026-11-22 — 取得資料（search）
- 6 次網路搜尋 + 2 次全文擷取（S3、S2）。
- 選出 6 篇：S1 原始論文、S2 綜述、S3 Anthropic 官方文章、S4 Lost in the Middle、S5 Ragas、S6 LLM Wiki。
- 淘汰：Medium／LinkedIn 等二手評論（來源不夠原始）。

## 2026-11-22 — Ingest ×6（一次一篇）
| 來源 | 新增/更新頁面 |
|---|---|
| S1 | what-is-rag、parametric-vs-nonparametric、hallucination-and-limits、embeddings-vector-search |
| S2 | rag-paradigms、indexing-chunking、rag-vs-finetuning-vs-long-context、rag-evaluation、hallucination-and-limits、what-is-rag |
| S3 | contextual-retrieval、bm25-hybrid-search、reranking-topk、indexing-chunking、rag-vs-finetuning-vs-long-context |
| S4 | lost-in-the-middle、reranking-topk、rag-vs-finetuning-vs-long-context |
| S5 | rag-evaluation |
| S6 | rag-vs-llm-wiki |
- 每篇 ingest 後更新 index.md。

## Lint #1 → 1 個錯誤
- W5：rag-paradigms 的「3」找不到出處 → 原因是檢查器把「## 3. Modular RAG」的標題編號當成數字（**檢查器誤報**）。修正檢查器，Lint #2 通過。

## Query → 產生簡報 v1（16 頁）
- 每頁標 data-wiki（用到哪幾個 wiki 頁）與頁尾出處。

## 簡報檢查 #1 → 49 個錯誤
- 14：章節編號「01–14」被當成數字（檢查器誤報）
- 1：跨元素文字黏在一起（檢查器誤報）
- 33：作者／年份／論文標題（Lewis、Gao、NeurIPS、2020…）不在該頁標註的概念頁 → 引用的來源頁沒被納入檢查範圍
- **1：封面寫「15 分鐘看懂」——Wiki 沒有這個數字，是生成時自己加的（真錯誤）**

## 修正
- 檢查器 v2：忽略章節編號、元素間加分隔、投影片引用 [S#] 時自動把 sources/S# 納入檢查範圍。
- **把檢查往前移**：新增 W7 規則（每個來源頁必須有年份與網址），在 ingest/lint 階段就檢查。
- W7 第一次跑仍通過 → 發現年份被檔名 raw/S2-gao-2023… 騙過（檢查器漏報），修正後 S2 被抓出缺年份 → 補上。
- 刪掉封面「15 分鐘」。

## 簡報檢查 #2–#4 → 0 個錯誤；Wiki Lint #6 → 0 個錯誤
- 變異測試：故意插入「準確率可提升 80%（Google 研究）」→ 檢查器正確抓到 2 個錯誤。
- 截圖檢查：封面深色背景被 CSS 權重蓋掉、導覽按鈕擋住頁尾 → 修正。
