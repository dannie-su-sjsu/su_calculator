#!/usr/bin/env python
# coding: utf-8

# In[5]:


# tests/test_trigonometry.py

import unittest
from calculator import sin, cos, tan
import math

class TestTrigonometry(unittest.TestCase):
    # Sin testing
    def test_sin(self):
        self.assertEqual(sin(30), math.sin(math.radians(30)))

    # Cos testing
    def test_cos(self):
        self.assertEqual(cos(30), math.cos(math.radians(30)))

    # Tan testing
    def test_tan(self):
        self.assertEqual(tan(30), math.tan(math.radians(30)))

if __name__ == '__main__':
    unittest.main(argv = [''], exit = False)


# In[ ]:




