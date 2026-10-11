# SIH26108 – AI-Powered Recommendation Engine for Identifying Applicable Indian Standards for Procurement Specifications

- **PS id:** SIH26108
- **Organization:** Ministry of Consumer Affairs, Food & Public Distribution (DoCA)
- **Theme:** Smart Automation | **Track:** Software

Paste a procurement specification; get ranked applicable standards with scores and matched terms.

## Requirements → code

| Requirement | Where |
|---|---|
| Accept free-text procurement spec | `POST /api/recommend`, textarea in `templates/index.html` |
| Identify applicable standards | `recommender.Recommender` – TF-IDF (1–2 grams) + cosine similarity (scikit-learn) |
| Standards catalogue | `data/sample_standards.json` (30 **sample** entries) |
| Ranked, explainable output | score + `matched_terms` per result |

## Run locally
```
pip install -r requirements.txt
python app.py          # http://127.0.0.1:5003
pip install pytest && pytest
```
Example: `curl -s -X POST localhost:5003/api/recommend -H 'Content-Type: application/json' -d '{"spec":"LED street light luminaires"}'`

## Limitations
The catalogue is **30 made-up sample entries** with ids like `SAMPLE-001`; they are not real Bureau of Indian Standards (BIS) texts or IS numbers. TF-IDF is lexical only (no semantic embeddings, no clause-level matching). Do not use for real procurement decisions.
