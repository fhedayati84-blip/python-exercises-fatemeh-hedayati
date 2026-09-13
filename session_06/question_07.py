# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:12:10 2026

@author: Fatemeh
"""

orders = [
    ("Ali", "Laptop"),
    ("Sara", "Phone"),
    ("Ali", "Phone"),
    ("Reza", "Laptop"),
    ("Sara", "Laptop"),
    ("Ali", "Tablet"),
    ("Reza", "Phone")
]

customer_products = {}

for customer, product in orders:

    if customer in customer_products:
        customer_products[customer].append(product)

    else:
        customer_products[customer] = [product]

print(customer_products)