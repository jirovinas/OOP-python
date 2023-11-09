class Clothing:
    def __init__(self, item_name, price, size) -> None:
        self.item_name = item_name
        self.price = price 
        self.size = size

    def get_description(self):
        return f"Name: {self.item_name}, Price: {self.price}, Size: {self.size}"

    def get_price(self):
        return self.price
    
class Customer:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.purchases = []
    def purchase_clothing(self, clothing):
        self.purchases.append(clothing)

    def get_purchase_history(self):
        info = ""
        for every_item in self.purchases:
            info += f"{every_item.get_description()} \n"
        return info
    
class Cashier:
    def __init__(self, name) -> None:
        self.name = name

    def generate_receipt(self, customer):
        total_cost = sum(item.get_price() for item in customer.purchases)
        receipt = f"Customer: {customer.name}\nEmail: {customer.email}\nPurchase History:\n"
        for every_description in customer.purchases:
            receipt += f"{every_description.get_description()}\n"
        receipt += f"\nTotal Cost: ${total_cost}\nServed by: {self.name}" 
        return receipt




# Create Clothing objects
shirt = Clothing("Blue Shirt", 20, "M")
jeans = Clothing("Denim Jeans", 30, "L")
hat = Clothing("Sun Hat", 15, "One Size")

#Create a Customer
customer = Customer("Alice", "alice@example.com")

# # Make clothing purchases
customer.purchase_clothing(shirt)
customer.purchase_clothing(jeans)
customer.purchase_clothing(hat)

# # Create a Cashier
cashier = Cashier("John")

# # Generate a receipt
receipt = cashier.generate_receipt(customer)
print(receipt)


