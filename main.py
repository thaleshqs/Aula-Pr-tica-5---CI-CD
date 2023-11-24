class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        result = x + y
        self.memory = result
        return result

    def subtract(self, x, y):
        result = x - y
        self.memory = result
        return result

    def multiply(self, x, y):
        result = x * y
        self.memory = result
        return result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Can't divide by zero")
        result = x / y
        self.memory = result
        return result

    def power(self, x, y):
        result = x ** y
        self.memory = result
        return result

    def get_memory(self):
        return self.memory
    
    def reset_memory(self):
        self.memory = 0