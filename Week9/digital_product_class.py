from product_class import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_fulfilment_info(self):
        return f"The product is delivered digitally"

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")