from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Product: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock} units")