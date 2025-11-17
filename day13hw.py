import os

filename = "students.txt"

count = int(input("How many student names do you want to add? "))

if os.path.exists(filename):
    print("Existing names:")
    with open(filename, "r") as f:
        print(f.read())

with open(filename, "a") as f:
    for _ in range(count):
        name = input("Enter student name: ")
        f.write(name + "\n")

print("Updated list of students:")
with open(filename, "r") as f:
    print(f.read())
