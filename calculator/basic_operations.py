#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# calculator/basic_operations.py
# Add
def add(x, y):
  return x + y

# Subtract
def subtract(x, y):
  return x - y

# Multiply
def multiply(x, y):
  return x * y

# Divide
def divide(x, y):
  if y == 0:
    raise ZeroDivisionError("Can't divide by zero.")
  else:
    return x / y

