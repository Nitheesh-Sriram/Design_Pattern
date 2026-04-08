from abc import ABC, abstractmethod

# 🔹 Strategy Interface
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, distance, time):
        pass


# 🔹 Concrete Strategies
class NormalPricing(PricingStrategy):
    def calculate_fare(self, distance, time):
        return distance * 10 + time * 2


class SurgePricing(PricingStrategy):
    def calculate_fare(self, distance, time):
        return (distance * 10 + time * 2) * 1.5


class PremiumPricing(PricingStrategy):
    def calculate_fare(self, distance, time):
        return (distance * 20 + time * 5)


# 🔹 Context
class FareCalculator:
    def __init__(self, strategy: PricingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PricingStrategy):
        self.strategy = strategy

    def calculate(self, distance, time):
        return self.strategy.calculate_fare(distance, time)


# 🔹 Usage
fare = FareCalculator(NormalPricing())
print("Normal Fare:", fare.calculate(10, 15))

fare.set_strategy(SurgePricing())
print("Surge Fare:", fare.calculate(10, 15))

fare.set_strategy(PremiumPricing())
print("Premium Fare:", fare.calculate(10, 15))