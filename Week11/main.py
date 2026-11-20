from pathlib import Path
from bulkDiscount import BulkDiscount
from percentageDiscount import PercentageDiscount
from inventory import Inventory
from order import Order
from productLoader import load_products
from supplier import Supplier


def main() -> None:
    supplier = Supplier("S01", "Lab Supplier", "supplier@example.com")
    inventory = Inventory()

    csv_path = Path(__file__).resolve().parent / "product.csv"
    load_products(str(csv_path), inventory, supplier)
    inventory.display_all()

    product = inventory.find_product("P001")
    if product is None:
        print("Cannot demonstrate the order: P001 was not loaded.")
        return

    order = Order("O001", BulkDiscount(200, 20))
    order.add_order_line(product, 10)

    print(f"Bulk discount total: ${order.calculate_total():.2f}")

    order.set_discount(PercentageDiscount(10))
    print(f"Percentage discount total: ${order.calculate_total():.2f}")


if __name__ == "__main__":
    main()