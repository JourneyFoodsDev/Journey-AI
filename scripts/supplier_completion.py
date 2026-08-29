from quality_lib import rate, write_report

FIELDS = ["name", "email", "country", "certifications", "ingredientsCount"]


def score(rows: list[dict]) -> dict:
    return {"entity": "supplier", "fields": FIELDS, **rate(rows, FIELDS)}


if __name__ == "__main__":
    print(write_report("supplier_completion", score([])))
