import unittest
from app import add, subtract, multiply, divide
 
class TestAddition(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(10, 20), 30)
    
    def test_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-10, -20), -30)
    
    def test_mixed_numbers(self):
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-10, 5), -5)
 
class TestSubtraction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(20, 10), 10)
    
    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -2), -3)
        self.assertEqual(subtract(-10, -20), 10)
    
    def test_mixed_numbers(self):
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(-10, 5), -15)
 
class TestMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(10, 5), 50)
    
    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(-10, -5), 50)
    
    def test_mixed_numbers(self):
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-10, 5), -50)
 
class TestDivision(unittest.TestCase):
    def test_integer_division(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(10, 2), 5)
    
    def test_float_division(self):
        self.assertEqual(divide(5, 2), 2.5)
        self.assertAlmostEqual(divide(1, 3), 0.333, places=3)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)
 
    def test_divide_by_negative(self):
        self.assertEqual(divide(10, -2), -5)
        self.assertAlmostEqual(divide(8, 4), -2)
 
if __name__ == '__main__':
    unittest.main()
