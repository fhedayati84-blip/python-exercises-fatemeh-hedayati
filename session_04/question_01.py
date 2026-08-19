import random
number=random.random()
print(number)
while True:
    hads=float(input("لطفا یک عدد حدس بزنید و وارد کنید"))
    if hads>number:
        print("عدد کوچک تر است")
    elif hads<number:
        print("عدد بزرگ تر است")
    elif hads==number:
        print("بله .درست گفتید")
        break
