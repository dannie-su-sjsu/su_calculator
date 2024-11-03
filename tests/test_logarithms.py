#!/usr/bin/env python
# coding: utf-8

# In[4]:


# tests/test_logarithms.py

import unittest
from calculator import log, ln, exponential
import math

class TestLogarithms(unittest.TestCase):
    # Log testing
    def test_log(self):
        self.assertEqual(log(10), math.log(10, 10))
        self.assertEqual(log(20, 2), math.log(20, 2))

    # Ln testing
    def test_ln(self):
        self.assertEqual(ln(5), math.log(5))

    # Exponential testing
    def test_exponential(self):
        self.assertEqual(exponential(10), math.exp(10))

if __name__ == '__main__':
    unittest.main(argv = [''], exit = False)


# In[ ]:




