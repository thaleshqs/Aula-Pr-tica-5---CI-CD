import unittest
import sys
sys.path.append("..")
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(5, 3)
        self.assertEqual(result, 8)
        self.assertEqual(self.calculator.get_memory(), 8)

    def test_subtraction(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6)
        self.assertEqual(self.calculator.get_memory(), 6)

    def test_multiplication(self):
        result = self.calculator.multiply(2, 6)
        self.assertEqual(result, 12)
        self.assertEqual(self.calculator.get_memory(), 12)

    def test_division(self):
        result = self.calculator.divide(8, 2)
        self.assertEqual(result, 4)
        self.assertEqual(self.calculator.get_memory(), 4)

    def test_power(self):
        result = self.calculator.power(2, 3)
        self.assertEqual(result, 8)
        self.assertEqual(self.calculator.get_memory(), 8)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

    def test_memory_usage(self):
        self.calculator.add(5, 3)
        memory_value = self.calculator.get_memory()
        result_using_memory = self.calculator.add(memory_value, 5)
        self.assertEqual(result_using_memory, 13)

if __name__ == '__main__':
    unittest.main()
