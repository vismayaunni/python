import random
import math

names = input("Enter customer names (comma-separated): ")

name_list = [n.strip() for n in names.split(",") if n.strip() != ""]
unique_names = list(set(name_list))

random.shuffle(unique_names)

winners = random.sample(unique_names, 2)

rev1 = winners[0][::-1]
rev2 = winners[1][::-1]

print("Winner 1 (reversed):", rev1)
print("Winner 2 (reversed):", rev2)

count = len(unique_names)
print("Total unique participants:", count)
print("Square root (rounded):", round(math.sqrt(count)))
