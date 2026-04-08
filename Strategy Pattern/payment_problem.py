from abc import ABC, abstractmethod

# 🔹 Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# 🔹 Concrete Strategies
class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")
        print("Validating UPI ID...")
        print("Payment successful via UPI ✅")


class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing Card payment of ₹{amount}")
        print("Checking card details...")
        print("Payment successful via Card 💳")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing PayPal payment of ₹{amount}")
        print("Redirecting to PayPal...")
        print("Payment successful via PayPal 🌐")


# 🔹 Context
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# 🔹 Usage
processor = PaymentProcessor(UPIPayment())
processor.process_payment(500)

processor.set_strategy(CardPayment())
processor.process_payment(1000)

processor.set_strategy(PayPalPayment())
processor.process_payment(2000)