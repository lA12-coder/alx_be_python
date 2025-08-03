from simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method"""
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-2,3),1)
    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(2,3),-1)
        self.assertEqual(self.calc.subtract(-1,-1),0)
    def test_multiply(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(2,3),6)
        self.assertEqual(self.calc.multiply(-3,-5), 15)
        self.assertEqual(self.calc.multiply(-20,5), -100)
    def test_divide(self):
        """Test the division method"""
        self.assertEqual(self.calc.divide(8,2),4)
        self.assertEqual(self.calc.divide(-20,-5), 4)
        self.assertEqual(self.calc.divide(-20,5), -4)
        self.assertEqual(self.calc.divide(2,0), None)
        
            