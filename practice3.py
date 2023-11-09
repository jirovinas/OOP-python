class ClothingItem:
    def __init__(self, name, category, color) -> None:
        self.name = name
        self.category = category
        self.color = color

    def __str__(self) -> str:
        return f"Clothing: {self.name} Category: {self.category} Color: {self.color}"

class Wardrobe:
    def __init__(self) -> None:
        self.clothing_items = []
    
    def add_item(self, item):
        self.clothing_items.append(item)

    def remove_item(self, item):
        self.clothing_items.remove(item)

    def get_items_by_category(self, category):
        matching_items = []
        for item in self.clothing_items:
            if item.category == category:
                matching_items.append(item)
        return matching_items
    
    def __str__(self) -> str:
        result = f"Outfit:\nClothing Items:\n"
        for item in self.clothing_items:
            result += str(item) 
        return result


class Outfit:
    def __init__(self, name) -> None:
        self.name = name
        self.clothing_items = []

    def add_item(self, item):
        self.clothing_items.append(item)

    def remove_item(self, item):
        self.clothing_items.remove(item)

    def __str__(self) -> str:
        result = f"Outfit: {self.name}\nClothing Items:\n"
        for item in self.clothing_items:
            result += str(item) 
        return result

# Create instances of clothing items, a wardrobe, and an outfit
shirt1 = ClothingItem("Blue Shirt", "Shirt", "Blue")
pants1 = ClothingItem("Jeans", "Pants", "Black")
shoes1 = ClothingItem("Sneakers", "Shoes", "White")

wardrobe = Wardrobe()
wardrobe.add_item(shirt1)
wardrobe.add_item(pants1)
wardrobe.add_item(shoes1)

outfit1 = Outfit("Casual Outfit")
outfit1.add_item(shirt1)
outfit1.add_item(pants1)
outfit1.add_item(shoes1)


# Display information
print(wardrobe)
print(outfit1)
