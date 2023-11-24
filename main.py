from calculator.calculator import Calculator

if __name__ == "__main__":
    #exemplos de uso
    calculator = Calculator()
    result_addition = calculator.add(5, 3)
    result_subtraction = calculator.subtract(10, 4)
    result_multiplication = calculator.multiply(2, 6)
    result_division = calculator.divide(8, 2)
    result_power = calculator.power(2, 3)

    print("Addition:", result_addition)
    print("Subtraction:", result_subtraction)
    print("Multiplication:", result_multiplication)
    print("Division:", result_division)
    print("Power:", result_power)

    memory_value = calculator.get_memory()
    result_using_memory = calculator.add(memory_value, 5)
    print("Result using memory:", result_using_memory)
