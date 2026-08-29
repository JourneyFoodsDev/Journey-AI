from quality_lib import rate, write_report

FIELDS = ["name", "brand", "formula", "nutrition", "claims", "packaging", "status"]


def score(rows: list[dict]) -> dict:
    return {"entity": "product", "fields": FIELDS, **rate(rows, FIELDS)}


if __name__ == "__main__":
    print(write_report("product_completion", score([])))
