from quality_lib import rate, write_report

FIELDS = ["name", "material", "weight", "recyclable", "supplier"]


def score(rows: list[dict]) -> dict:
    return {"entity": "packaging", "fields": FIELDS, **rate(rows, FIELDS)}


if __name__ == "__main__":
    print(write_report("packaging_completion", score([])))
