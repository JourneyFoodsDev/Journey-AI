from ingredient_completion import score as ingredients
from packaging_completion import score as packaging
from product_completion import score as products
from quality_lib import write_report
from supplier_completion import score as suppliers


def main() -> None:
    report = {
        "ingredients": ingredients([]),
        "products": products([]),
        "packaging": packaging([]),
        "suppliers": suppliers([]),
    }
    print(write_report("quality-report", report))


if __name__ == "__main__":
    main()
