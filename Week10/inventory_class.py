from product_class import Product
from physical_product_class import PhysicalProduct
from digital_product_class import DigitalProduct
from supplier_class import Supplier

class Inventory:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def display_all(self) -> None:
            print("=====================================================")
            for product in self.products:
                product.display_information()
            print("=====================================================\n")

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        print("Product added successfully.\n")

    def remove_product(self, product_id: str) -> None:
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print("Product removed successfully.\n")
                return
        print("Product not found.\n")

    def update_stock(self, product_id: str, quantity: int) -> None:
        for product in self.products:
            if product.product_id == product_id:
                product.update_stock(quantity)
                print("Stock updated successfully.\n")
                return
        print("Product not found.\n")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                print("Product found!\n")
                return product
        return None