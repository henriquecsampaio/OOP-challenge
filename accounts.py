from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, agency, number, balance):
        self.agency = agency
        self.number = number
        self.balance = balance

    def deposit(self, quantity):
        self.balance += quantity
        self.details()

    def details(self):
        print(f"Agency : {self.agency}"
              f"Number : {self.number}"
              f"Balance : {self.balance}")

    @abstractmethod
    def withdraw(self, value):
        pass


class Savings(Account):

    def withdraw(self, value):
        if self.balance < value:
            print("Insufficient funds!")
            return
        self.balance -= value
        self.details()


class ContaCorrente(Account):

    def __init__(self, agency, number, balance, limit=100):
        super().__init__(agency, number, balance)
        self.limit = limit

    def withdraw(self, value):
        if (self.balance + self.limit) < value:
            print("Insufficient funds!")
            return
        self.balance -= value
        self.details()
