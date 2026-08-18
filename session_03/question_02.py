""" barname benevisid ke 10 bar ertfae parsh varzeshkar ra daryaft kond
agar record jadid bodpayam bishtarin parsh sabt shod namayash dade shavad
agar qhabla sabt shode bod payam monasbat chap shavad"""

record=0
for i in range(10):
    height=float(input(f"{i+1}ارتفاع پرش را وارد کنید:"))
    if height>record:
        record=height
        print("!رکورد جدید بیشترین پرتاب ثبت شد:{record}")
    elif height== record:
        print("این ارتفاع برابر با رکورد قبلی است")
    else:
        print("رکورد جدیدی ثبت نشد")
