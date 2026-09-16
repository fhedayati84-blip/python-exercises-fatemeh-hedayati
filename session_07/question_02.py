def process_order(customer, *products, **options):
    prices = {"Laptop": 50000000,"Mouse": 500000,"Keyboard": 1000000 }

    discount = options.get("discount", 0)
    tax = options.get("tax", 9)
    shipping = options.get("shipping", 0)
    total_price = 0
    for product in products:
        total_price += prices.get(product, 0)
    discount_amount = total_price * discount / 100
    price_after_discount = total_price - discount_amount
    tax_amount = price_after_discount * tax / 100
    final_price = price_after_discount + tax_amount + shipping
    return {"customer": customer,"products": list(products),"discount": discount,
        "tax": tax,"shipping": shipping,"final_price": final_price}


result = process_order("Ali","Laptop","Mouse","Keyboard",discount=10,tax=9,
shipping=2000000
)
print(result)