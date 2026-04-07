class ResponseStrategy:
    def generate(self, input_text):
        pass

class FormalStrategy(ResponseStrategy):
    def generate(self, input_text):
        return "Good evening " + input_text


class CasualStrategy(ResponseStrategy):
    def generate(self, input_text):
        return "Hey! " + input_text


class TechnicalStrategy(ResponseStrategy):
    def generate(self, input_text):
        return "From a technical perspective " + input_text



class AIResponseSystem:
    def __init__(self, strategy: ResponseStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ResponseStrategy):
        self.strategy = strategy




def generate_response(self, input_text):
    return self.strategy.generate(input_text)




ai = AIResponseSystem(FormalStrategy())
print(ai.generate_response("your request is processed"))

ai.set_strategy(CasualStrategy())
print(ai.generate_response("done"))

ai.set_strategy(TechnicalStrategy())
print(ai.generate_response("task executed"))