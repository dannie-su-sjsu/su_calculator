#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# calculator/complex_numbers.py
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real_result = self.real * other.real - self.imaginary * other.imaginary # (ac - bd)
        imaginary_result = self.real * other.imaginary + self.imaginary * other.real # (ad + bc)
        return Complex(real_result, imaginary_result)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2 # (c^2 + d^2)
        if denominator == 0:
            raise ZeroDivisionError("Can't divide by zero.")
        real_result = (self.real * other.real + self.imaginary * other.imaginary) / denominator # (ac + bd) / (c^2 + d^2)
        imaginary_result = (self.imaginary * other.real - self.real * other.imaginary) / denominator # (bc - ad) / (c^2 + d^2)
        return Complex(real_result, imaginary_result)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

