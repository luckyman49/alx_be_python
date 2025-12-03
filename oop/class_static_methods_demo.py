# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b. Does not use class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Print the class calculation_type and return the product."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
