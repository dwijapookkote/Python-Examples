# -*- coding: utf-8 -*-
"""day2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H5Ols5aVeXrUZ6MMDGKd0cpNNvOB2TOM
"""

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior")