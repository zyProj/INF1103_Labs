from abc import ABC, abstractmethod
from supplier_class import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.product_id: str = product_id
        self.name: str = name
        self.price: float = price
        self.stock: int = stock
        self.supplier: Supplier = supplier

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def update_stock(self, quantity: int) -> None:
        self.stock = quantity

    def display_information(self) -> None:
        print(f"ID: {self.product_id} | Product: {self.name} | "
              f"Price: ${self.price:.2f} | Stock: {self.stock} units | "
              f"Supplier: {self.supplier.name}")