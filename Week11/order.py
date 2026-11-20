from product import Product
#from physical_product_class import PhysicalProduct
#from digital_product_class import DigitalProduct
from orderline import OrderLine
from discountStrategy import DiscountStrategy, NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount = NoDiscount() if discount is None else discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def calculate_total(self) -> float:
        total = sum(
            order_line.calculate_subtotal()
            for order_line in self.order_lines
        )
        return self.discount.apply(total)