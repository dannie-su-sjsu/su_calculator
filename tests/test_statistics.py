#!/usr/bin/env python
# coding: utf-8

# In[8]:


# tests/test_statistics.py

import unittest
from calculator import mean, mode, median, std_dev
import statistics

class TestStatistics(unittest.TestCase):
    # Mean testing
    def test_mean(self):
        self.assertEqual(mean([5, 10, 15]), 10)

    # Mode testing
    def test_mode(self):
        self.assertEqual(mode([5, 10, 10, 15]), 10)

    # Median testing
    def test_median(self):
        self.assertEqual(median([2, 4, 6, 8, 10]), 6)
        self.assertEqual(median([2, 4, 6, 8]), 5)

    # Standard Deviation testing
    def test_std_dev(self):
        self.assertEqual(std_dev([10, 20, 30, 40]), statistics.stdev([10, 20, 30, 40]))

if __name__ == '__main__':
    unittest.main(argv=[''], exit = False)


# In[ ]:




