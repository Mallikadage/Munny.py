from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


# UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


# Cash Payment
class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash.")


# Creating objects
credit = CreditCardPayment()
upi = UPIPayment()
cash = CashPayment()

# Calling methods
credit.pay(5000)
upi.pay(1500)
cash.pay(800)