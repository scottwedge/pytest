class CalculatorError(Exception):
    pass 

class CalculatorZeroDivError(Exception):
    pass


class Calculator():
    """ A terrible calculator design """

    def add(self, x, y):
        try:
            return x + y
        except TypeError:
            raise CalculatorError
        except ZeroDivisionError:
#            raise CalculatorZeroDivError
             pass

    def subtract(self, x, y):
        return x - y


    def multiply(self, x, y):
        return x * y


    def divide(self, x, y):
        return x / y


