# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:16:11 2026

@author: Fatemeh
"""

products = {"P01": ("Laptop", 1200, 5),"P02": ("Phone", 800, 0),"P03": ("Tablet", 500, 12),
 "P04": ("Mouse", 50, 25),
 "P05": ("Keyboard", 100, 0)
}

total_warehouse = 0
max_value = 0
max_product = ""

for code, product in products.items():

    name, price, stock = product

    if stock > 0:
        print("موجود:", name)

    if stock == 0:
        print("ناموجود:", name)

    value = price * stock
    print("ارزش موجودی", name, "=", value)

    total_warehouse += value

    if value > max_value:
        max_value = value
        max_product = name


print("بیشترین ارزش موجودی:", max_product, max_value)
print("ارزش کل انبار:", total_warehouse)