
class Item:
    def __init__(self,price,discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self):
        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price,self.price_after_discount())


def on_sale_discount(order):
    return order.price * 0.25 + 20

def twenty_percent_discount(order):
    return order.price * 0.20

if __name__=="__main__":
    print(Item(20000))
    print(Item(20000,discount_strategy=twenty_percent_discount))
    print(Item(20000, discount_strategy=on_sale_discount))