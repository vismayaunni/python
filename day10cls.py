from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, year_joined):
        self.name = name
        self.year_joined = year_joined

    def years_on_platform(self):
        return 2025 - self.year_joined

    @abstractmethod
    def get_role(self):
        pass

    def print_user_message(self):
        print(f"Name: {self.name}, Role: {self.get_role()}, Years on Platform: {self.years_on_platform()}")

class Customer(User):
    def get_role(self):
        return "Customer"

class Vendor(User):
    def get_role(self):
        return "Vendor"

c = Customer("Priya", 2020)
v = Vendor("Arjun", 2015)

c.print_user_message()
v.print_user_message()