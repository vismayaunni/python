item = input("Enter a new item: ")

import os

filename = "items.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write(item + "\n")
else:
    with open(filename, "a") as f:
        f.write(item + "\n")

with open(filename, "r") as f:
    print(f.read())
