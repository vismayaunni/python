fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Potato"]
beverages = ["Juice", "Water", "Soda"]
fruits.append("Mango")
vegetables.insert(1, "Onion")
beverages.pop()
inventory = [fruits, vegetables, beverages]
print(fruits[:2])
print(vegetables[-1])
fruit_lengths = [len(item) for item in fruits]
print(fruit_lengths)
print("Water" in beverages)
first_items = (fruits, vegetables, beverages)
print(first_items)