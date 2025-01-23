
class Calculator:
    name = "Good Calculator"
    
    def add(self, x, y):
        print(self.name)
        result = x + y
        print(result)
    
    def sub(self, x, y):
        print(self.name)
        result = x - y
        print(result)

    def mul(self, x, y):
        print(self.name)
        result = x * y
        print(result)

    def div(self, x, y):
        print(self.name)
        result = x / y
        print(result)
    
    def test(x, y):
        print(x, y)

calculator = Calculator()

print(calculator.name)
calculator.add(10, 20)