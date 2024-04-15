import unittest
from app import add, subtract, multiply
 
class TestAddition(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(10, 20), 30)
    
    def test_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-10, -20), -30)
    
 
class TestSubtraction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(20, 10), 10)
    
    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -2), -3)
        self.assertEqual(subtract(-10, -20), 10)
    
class TestMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(10, 5), 50)
    
    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(-10, -5), 50)
    
 
if __name__ == '__main__':
    unittest.main()
