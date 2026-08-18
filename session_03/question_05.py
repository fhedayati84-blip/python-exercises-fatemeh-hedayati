"""barnameh benevis ke be mashin hesab sade amal konad az karbar do adad 
bagarad va yak amaliat reyazi (+,-,/,*) daryaft konad natige mohasebeh
 konad"""


a=float(input("enter first num:"))
b=float(input("enter sacond num:"))
operator=input("enter operator (+,-,*,/):")
if operator =="+":
    print(a+b)
elif operator =="-":
    print(a-b)
elif operator =="*":
    print(a*b)
elif operator =="/":  
  if b!=0:
      print(a/b)
  else:
      print("تقسیم بر صفر امکان ندارد ")
else: 
     print("عملگر نامعتبر است")
     
     
