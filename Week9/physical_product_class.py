from product_class import Product
from can_be_shipped_interface import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_fulfilment_info(self):
        return f"The product requires physical shipping"

    def calculate_shipping_cost(self):
        shipping_rate_per_kg = 0.2
        return self.__weight * shipping_rate_per_kg

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")