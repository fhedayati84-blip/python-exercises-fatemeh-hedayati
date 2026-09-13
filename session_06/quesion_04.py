
employees = {
    "E01": {"name": "Ali","age": 28,"salary": 3000},
    "E02": {"name": "Sara","age": 32,"salary": 4500},
    "E03": {"name": "Reza","age": 25,"salary": 2800}
}

sum = 0
b= 0
highest_name = ""

a = 100000000
lowest_name = ""

for i in employees.values():

    salary = i["salary"]
    name = i["name"]

    sum = sum + salary

    if salary > b:
        b = salary
        highest_name = name

    if salary < a:
        a = salary
        lowest_name = name

    if salary > 3000:
        print("حقوق بیشتر از 3000:", name)

average = sum / len(employees)

print("بیشترین حقوق:", highest_name,":", b)
print("میانگین حقوق:", average)
print("کمترین حقوق:", lowest_name,":", b)

