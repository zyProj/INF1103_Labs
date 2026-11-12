from product_class import Product
from supplier_class import Supplier
from can_be_shipped_interface import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.weight: float = weight

    def get_fulfilment_info(self) -> str:
        return f"The product requires physical shipping"

    def calculate_shipping_cost(self) -> float:
        shipping_rate_per_kg = 0.2
        return self.weight * shipping_rate_per_kg

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.weight} kg")