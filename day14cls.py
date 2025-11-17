
import random
import math

names = input("Enter guest names (comma-separated): ")

name_list = [n.strip() for n in names.split(",") if n.strip() != ""]
unique_names = list(set(name_list))

chosen = random.choice(unique_names)
reversed_name = chosen[::-1]

print("Randomly selected guest:", chosen)
print("Reversed name:", reversed_name)

count = len(unique_names)
print("Total unique names:", count)
print("Rounded square root:", round(math.sqrt(count)))
```
