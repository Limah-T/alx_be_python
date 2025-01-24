class Calculator:
    calculation_type = "Arithmetric Operations"

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculator_type}")
        return a * b
    
    @staticmethod
    def add(a, b):
        return a + b
    