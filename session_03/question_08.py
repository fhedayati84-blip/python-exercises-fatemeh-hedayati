"""barnameh benevisid ke mojodi hesab va mablagh bardasht ra daryaft  konid 
agar mablagh bardasht mosbat bod agar mojodi cofi bid amaliat bardasht
anjam shavad dar gheir in sorat in payam mojodi na cafi namayash  dadeh shavad
agar mablagh bardasht manfi ya sefr bod payam khata namayash dade shavad"""


accound_balance=float(input("موجودی حساب وارد کنید :"))
withdraw_amount=float(input("مبلغ برداشت وارد کید :"))
if withdraw_amount>0 and withdraw_amount <= accound_balance:
    print(accound_balance-withdraw_amount)
    print("عملیات برداشت انجام شد")
else:
    print("موجودی کافی نیست ")
    if withdraw_amount <=0:
        print("خطا")