# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:14:43 2026

@author: Fatemeh
"""

text = input("یک رشته وارد کنید: ")

letters = {}

for i in text:

    if i.isalpha():

        if i in letters:
            letters[i] += 1

        else:
            letters[i] = 1

print(letters)
