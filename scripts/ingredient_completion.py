"""Ingredient completion for Admin Data + AI Ingredients Agent."""

from quality_lib import rate, write_report

FIELDS = [
    "name",
    "supplier",
    "category",
    "nutrition",
    "allergens",
    "sustainability",
    "price",
    "origin",
]


def score(rows: list[dict]) -> dict:
    summary = rate(rows, FIELDS)
    return {
        "entity": "ingredient",
        "fields": FIELDS,
        **summary,
        "flagHighImpact": [
            row.get("name")
            for row in rows
            if not row.get("nutrition") or not row.get("allergens")
        ][:25],
    }


if __name__ == "__main__":
    sample = []
    path = write_report("ingredient_completion", score(sample))
    print(path)
