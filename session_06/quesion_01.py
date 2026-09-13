# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:58:17 2026

@author: Fatemeh
"""

products = {"laptop":1200,"phone":800,"tablet":500,"headphone":150,"mouse":50}
a=list(products.values())
max_price = a[0]
min_price = a[0]
for i in products.values():
    if i > max_price:
        max_price=i
    if i<min_price:
        min_price=i
average = sum(products.values()) / len(products)
total=sum(products.values())
print("گران ترین محصول:" ,max_price) 
print("ارزان ترین محصول:",min_price)
print("میانگین قیمت محصولات:",average)
print("قیمت تمام محصولات :",total)
for i in products:
    if products[i]>500:
     print(f"{i}:{products[i]}")












 













