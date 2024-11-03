#!/usr/bin/env python
# coding: utf-8

# In[8]:


# tests/test_basic_operations.py

import unittest
from calculator import add, subtract, multiply, divide

class TestBasicOperations(unittest.TestCase):
    # Addition tests
    def test_add(self):
        self.assertEqual(add(1, 4), 5)
        self.assertEqual(add(3, 0), 3)
        self.assertEqual(add(2, -2), 0)
    # Subtraction tests
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(2, 0), 2)
        self.assertEqual(subtract(-1, -3), 2)
    # Multiplication tests
    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(3, 0), 0)
    # Division test
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(1, 4), 0.25)
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)
        
    
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)


# In[ ]:




