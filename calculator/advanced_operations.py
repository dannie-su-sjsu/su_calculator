#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# calculator/advanced_operations.py
import math

# Square
def square(x):
  return x * x

# Power of
def power(x, y):
  return x ** y

# Square root
def square_root(x):
  # Need to check if x is greater than 0
  return math.sqrt(x)

# Factorial
def factorial(x):
  if x <= 0:
    return 1
  else:
    return x * factorial(x - 1)

