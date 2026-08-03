# Truth Collective — Evaluation Engine v1

Built from Daniel’s `TC Master Summary Docment Cursor Copy.xls` + Official Master Multi-Stage Evaluation PDF v2.1.

## File
`TC_Evaluation_Engine_v1.xlsx`

## How to use
1. Open **02_Intake** — enter name, ASIN/URL, category, Product or Book.
2. Score **03_Engineering_Score** (products) or **04_Editorial_Score** (books). Set **Applicable = Y** only on relevant rows; enter Score 0–10.
3. Fill **05_Compliance** where it applies.
4. Read **07_Results** for TC Grade, quality band, publish recommendation, and auto brief analysis.

## Design rules
- Intelligence lives in **01_Master_Config** (weights + TC Grade bands).
- Products are **not** forced through 60% Eng / 40% Editorial (that was wrong for desks/monitors).
- Amazon stars are **not** the grade.
- ASIN/URL is tracking + later lookup — it does not invent engineering evidence.

## Still missing (optional later)
- Category presets that auto-flip Applicable rows
- Live ASIN title/price pull
- One-click HTML export for WordPress product tiles
- Extra category metrics from the full 179-page set (Monitors Delta E, etc. started in benchmarks tab)
