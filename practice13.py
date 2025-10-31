# abstraction in oop

from abc import ABC, abstractmethod # this is built in module

class vehicle(ABC):
    @abstractmethod # this is decorator it has no code only a definition
    def start_engine(self):
        pass  # this is placeholder used because python doesnt allow empty method bodies

class car(vehicle):
    def start_engine(self):
        print("Car Engine started with a Key.")

my_car = car()
my_car.start_engine()


# example payment system

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class creditcardpayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Credit card.")

class Upipayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")

p1 = creditcardpayment()
p1.pay(500)

p2 = Upipayment()
p2.pay(300)