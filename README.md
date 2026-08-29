# JourneyAI

Catalog quality jobs used by Admin → Data and Admin → Customers.

## Triggers

| Script | What it measures |
| --- | --- |
| `scripts/ingredient_completion.py` | Nutrition, supplier, allergen, sustainability field fill rate |
| `scripts/product_completion.py` | Formula, claims, brand, nutrition completeness |
| `scripts/packaging_completion.py` | Material, weight, recyclability |
| `scripts/supplier_completion.py` | Contact, location, certifications |
| `scripts/run_all.py` | Runs every job and writes `out/quality-report.json` |

## Run

```bash
export MONGO_URI="mongodb+srv://…"
python scripts/run_all.py
```

Admin UI should POST `/api/v1/ai/quality-run` on Node (or call these scripts from Cloud Run Job) per company.
