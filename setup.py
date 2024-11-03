#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# setup.py

import setuptools

setuptools.setup(
    name = "dannie_su_calculator_4360",
    version = "0.1.0",
    author = "Dannie Su",
    author_email = "dannie.su@sjsu.edu",
    description = "An advanced calculator package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/dannie-su-sjsu/su_calculator",
    packages = setuptools.find_packages(),
    python_requires = '>=3.13',
)

