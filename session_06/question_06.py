sales = (("Ali", "Laptop", 1200),("Sara", "Phone", 800),("Ali", "Phone", 800),
("Reza", "Laptop", 1200),("Sara", "Laptop", 1200),("Ali", "Mouse", 50)
)

customer_total = {}

for customer, product, price in sales:
    if customer in customer_total:
        customer_total[customer] += price
    else:
        customer_total[customer] = price

print("مجموع خرید هر مشتری:")
print(customer_total)


best_customer = None
max_total = 0

for customer, total in customer_total.items():
    if total > max_total:
        max_total = total
        best_customer = customer

print("بیشترین خرید:")
print(best_customer, max_total)


product_count = {}

for customer, product, price in sales:
    if product in product_count:
        product_count[product] += 1
    else:
        product_count[product] = 1

print("تعداد فروش هر محصول:")
print(product_count)


total_2 = 0

for customer, product, price in sales:
    total_2 += price

print(" درآمد فروشگاه:")
print(total_2)