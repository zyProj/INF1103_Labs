from product_class import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        print(f"ID: {self._Product__product_id} | Product: {self._Product__name} | Price: ${self._Product__price:.2f} | Stock: {self._Product__stock} units | Weight: {self.__weight} kg")