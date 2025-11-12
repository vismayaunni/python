class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        if isinstance(other, Account):
            return self._balance + other._balance
        return NotImplemented

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05

class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02

s1 = SavingsAccount("Ravi", 10000)
c1 = CurrentAccount("Anjali", 15000)

print(f"Name: {s1._name}, Balance: {s1._balance}, Interest: {s1.calculate_interest()}")
print(f"Name: {c1._name}, Balance: {c1._balance}, Interest: {c1.calculate_interest()}")
print(f"Total Balance: {s1 + c1}")