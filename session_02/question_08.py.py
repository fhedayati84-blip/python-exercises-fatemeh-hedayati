"""hour bein 0ta23 az karbar begirid va bazeh zamani roz (sobh,asr,zohr,shab)ra
tain namayid hamchenin agr adad kharj az bazeh bod payam khata chap namayid"""

a=int(input("(1ta23)hour ra vard konid:"))
if 1>a or 23<a:
    print("خطا :ساعت وارد شده صحیح نیست")
elif 12>a:
    print("صبح")
elif 14>a:
    print("ظهر")
elif 18>a:
    print("عصر")
else:
    print("شب")