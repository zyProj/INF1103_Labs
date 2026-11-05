from product_class import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_fulfilment_info(self):
        return f"The product requires physical shipping"
    
    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")