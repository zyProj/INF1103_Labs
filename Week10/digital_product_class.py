from product_class import Product
from supplier_class import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: int):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def get_fulfilment_info(self):
        return f"The product is delivered digitally"

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")