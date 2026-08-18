"""yek barname benevisid ta bein adad 1 ta 10 harekat konad agar fard bod
dar 5 zarb mishavad agagr adad zoj bod 5 vahed ezafe shavad va jam namayesh
dahid""" 


num=0
for i in range(1,11):
    if i%2==0:
        i=i+5     
        print(i)
        num=num+i
    elif i%2!=0:
        j=i*5
        print(j)
        num=num+j
print(num,':', "مجموع کل پس از تغییرات ")    
        