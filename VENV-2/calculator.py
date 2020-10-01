class CalculatorError(Exception):
    pass

class Calculator():
    """ A terrible calculator design """

    def add(self, x, y):
        try:
            return x + y
        except:
            raise CalculatorError("addition error")

    def subtract(self, x, y):
        return x - y


    def multiply(self, x, y):
        return x * y


    def divide(self, x, y):
        return x / y


