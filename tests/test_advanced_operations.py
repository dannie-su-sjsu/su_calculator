#!/usr/bin/env python
# coding: utf-8

# In[4]:


# tests/test_advanced_operations.py

import unittest
from calculator import square, square_root, power, factorial

class TestAdvancedOperations(unittest.TestCase):
    # Square testing
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(5), 25)
        self.assertEqual(square(10), 100)

    # Power testing
    def test_power(self):
        self.assertEqual(power(10, 0), 1)
        self.assertEqual(power(2, 5), 32)
        self.assertEqual(power(2, -1), 0.5)

    # Square root testing
    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)

    # Factorial testing
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
    
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)


# In[ ]:




