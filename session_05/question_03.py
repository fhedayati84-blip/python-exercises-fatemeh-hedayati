reshteh=input("enter string:")
english=0
upper=0
lower=0
number=0
space=0
special=0
for i in reshteh:
   if("A"<=i<="Z")or("a"<=i<="z"):
    english +=1
   if(i.isupper()):
    upper +=1
   if(i.islower()):
    lower +=1
   if(i.isdigit()):
    number +=1
   if(i.isspace()):
    space +=1
special=len(reshteh)-english-number-space
print(f"upper:{upper}")
print(f"lower:{lower}")
print(f"space:{space}")
print(f"number:{number}")
print(f"english:{english}")
print(f"special:{special}")

                     

