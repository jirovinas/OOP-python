class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def get_description(self):
        message = f"{self.name}, ${self.price}"
        print(message)
    
    def get_price(self):
        return f"${self.price}"

class Vendors:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_product(self):            
        for every_product in self.products:
            every_product.get_description()

    def sell_product(self, product_name, student):
        for every_product in self.products:
            if every_product.name == product_name.name:
                student.purchased_software.append(every_product)

class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.purchased_software = []

    def purchase_software(self, vendor, product_name):
        vendor.sell_product(product_name, self)

    def get_purchase_history(self):
        for every_product in self.purchased_software:
            every_product.get_description()


samsung = Product('samsung', 50)
asus = Product('asus', 20)

miko = Student("miko")

gem = Vendors('to')

gem.add_product(samsung)
gem.add_product(asus)

miko.purchase_software(gem, samsung)
miko.purchase_software(gem, asus)

miko.get_purchase_history()
