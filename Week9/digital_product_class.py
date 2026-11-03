from product_class import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        print(f"ID: {self._Product__product_id} | Product: {self._Product__name} | Price: ${self._Product__price:.2f} | Stock: {self._Product__stock} units | Download Size: {self.__download_size} MB")