class Burger:
    def __init__(self,size,toppings):
        self.size = size
        self.toppings = toppings
        self.price = 0

        if self.size == "small":
            self.prize = 20
        elif self.size == "medium":
            self.price = 30
        elif self.size == "large":
            self.price = 40
        for every_topping in toppings:
            self.price += 5

    def get_description(self):
        return f"{self.size} pizza with {self.toppings}"
    
    def get_price(self):
        return self.price
    
class Order:
    def __init__(self):
        self.burger_list = []

    def add_burger(self,burger):
        self.burger = burger
        self.burger_list.append(self.burger)

    def calculate_total(self):
        self.total = 0
        for every_order in self.burger_list:
            self.total += every_order.get_price()
    def get_order_summary(self):
        for every_info in self.burger_list:
            print(f"Order {every_info.get_description}")
        print(f"The total price is {self.total}")    

burger1 = Burger("large", ["hotdog", "egg", "ham"])
print(burger1.get_description())
print(burger1.get_price())

order1 = Order()
order1.add_burger(burger1)
order1.calculate_total()
order1.get_order_summary()
