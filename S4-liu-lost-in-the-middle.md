---
id: S4
title: Lost in the Middle: How Language Models Use Long Contexts
authors: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang
venue: arXiv 2307.03172 (2023); TACL vol. 12 (2024)
url: https://arxiv.org/abs/2307.03172
ingested: 2026-11-22
---
# 原始重點（ingest 時擷取，之後不修改）
- 測兩種任務：多文件問答（multi-document QA）與 key-value 檢索。
- 相關資訊放在輸入的開頭或結尾時表現最好；放在中間時表現明顯下降——即使是標榜長上下文的模型也一樣。
- 輸入的 context 越長，表現也大幅下降。
- 結論：目前的語言模型無法穩健地使用長輸入中的資訊；這和 RAG 很相關，因為 RAG 會把多份檢索文件塞進 context。
