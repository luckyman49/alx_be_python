import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)

    def test_division(self):
        # normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # division by zero should raise ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()

