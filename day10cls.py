from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, join_year):
        self.name = name
        self.join_year = join_year

    def years_on_platform(self):
        return 2025 - self.join_year

    @abstractmethod
    def show_role(self):
        pass

    def __str__(self):
        return f"{self.name} has been on the platform for {self.years_on_platform()} years."

class Customer(User):
    def show_role(self):
        return "Customer"

    def __str__(self):
        return f"{self.name} ({self.show_role()}) has been using the platform for {self.years_on_platform()} years."

class Vendor(User):
    def show_role(self):
        return "Vendor"

    def __str__(self):
        return f"{self.name} ({self.show_role()}) has been using the platform for {self.years_on_platform()} years."

c1 = Customer("Alice", 2021)
v1 = Vendor("Bob", 2019)

print(c1)
print(v1)
