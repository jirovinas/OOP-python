class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        self.price = 0

        if self.size == "small":
            self.price = 10

        elif self.size == "medium":
            self.price = 12
        
        elif self.size == "large":
            self.price = 15

        for anything in toppings:
            self.price += 2

    def get_description(self):
        return f"{self.size} pizza with {self.toppings} "
    def get_price(self):
        return self.price
    
class Order:
    def __init__(self):
        self.list_of_pizza = []

    def add_pizza(self,pizza):
        self.pizza = pizza
        self.list_of_pizza.append(self.pizza)
        print("Pizza has been added to your list")

    def calculate_total(self):
        self.total = 0
        for each_order in self.list_of_pizza:
            self.total += each_order.get_price()

    def get_order_summary(self):
        for every_info in self.list_of_pizza:
            print(f"Order {every_info.get_description}")
        print("--------------")
        print(f"The total price is {self.total}")

pizza1 = Pizza("small", ["peperoni", "hawaian"],)
print(pizza1.get_description())
print(pizza1.get_price())

pizza2 = Pizza("medium", ["peperoni", "hawaian", "hotdog", "itlog"],)
print(pizza2.get_description())
print(pizza2.get_price())

order1 = Order()
order1.add_pizza(pizza1)
order1.calculate_total()
order1.get_order_summary()

order2 = Order()
order2.add_pizza(pizza2)
order2.calculate_total()
order2.get_order_summary()



