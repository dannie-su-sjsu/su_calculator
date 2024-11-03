#!/usr/bin/env python
# coding: utf-8

# In[7]:


# tests/test_complex_numbers.py

import unittest
from calculator import Complex

class TestComplex(unittest.TestCase):
    def setUp(self):
        self.complex1 = Complex(3, 5)
        self.complex2 = Complex(2, 6)
    # Complex addition testing
    def test_add(self):
        result = self.complex1 + self.complex2
        self.assertEqual(result.real, 5)
        self.assertEqual(result.imaginary, 11)
    # Complex subtraction testing
    def test_subtract(self):
        result = self.complex1 - self.complex2
        self.assertEqual(result.real, 1)
        self.assertEqual(result.imaginary, -1)
    # Complex multiplication testing
    def test_multiply(self):
        result = self.complex1 * self.complex2
        self.assertEqual(result.real, -24)
        self.assertEqual(result.imaginary, 28)
    # Complex division testing
    def test_divide(self):
        result = self.complex1 / self.complex2
        self.assertEqual(result.real, 0.9)
        self.assertEqual(result.imaginary, -0.2)


if __name__ == '__main__':
    unittest.main(argv = [''], exit = False)


# In[ ]:




