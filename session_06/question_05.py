
students = {"Ali": [18, 17, 20],"Sara": [15, 19, 18],"Reza": [12, 14, 10],
 "Mina": [20, 20, 19]
}

b = ""
c = 0

for i in students:

    a = students[i]

    average = sum(a) / len(a)

    if average >= 15:
        status = "Passed"
    else:
        status = "Failed"
    highest = a[0]

    for grade in a:
        if grade > highest:
            highest = grade

    print(i)
    print("Average:", round(average, 2))
    print("Status:", status)
    print("Highest:", highest)
    print()

    if average > c:
        best_average = average
        b = i

print("Best Student:", b)
print("Highest Average:", round(c, 2))