"""barnameh beevis ke az karbar adad daryaft ta zamani KE Karbar sefr vard 
nakarde agar sefr vard kard jam adad hesab shavad"""

total=0
while True:
    number=int(input("یک عدد وارد کنید:"))
    if number ==0:
        break
    total += number
print("جمع اعداد:",total)