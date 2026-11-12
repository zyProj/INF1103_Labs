from product_class import Product
from physical_product_class import PhysicalProduct
from digital_product_class import DigitalProduct
from supplier_class import Supplier

class Inventory:
    def __init__(self):
        self.__products: list[Product] = [] 

    def display_all(self):
            print("=====================================================")
            for product in self.__products:
                product.display_information()
            print("=====================================================\n")

    def add_product(self, product: Product):
        self.__products.append(product)
        print("Product added successfully.\n")

    def remove_product(self, product_id: str):
        for product in self.__products:
            if product._Product__product_id == product_id:
                self.__products.remove(product)
                print("Product removed successfully.\n")
                return
        print("Product not found.\n")

    def update_stock(self, product_id: str, quantity: int):
        for product in self.__products:
            if product._Product__product_id == product_id:
                product.update_stock(quantity)
                print("Stock updated successfully.\n")
                return
        print("Product not found.\n")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product._Product__product_id == product_id:
                print("Product found!\n")
                return product
        return None