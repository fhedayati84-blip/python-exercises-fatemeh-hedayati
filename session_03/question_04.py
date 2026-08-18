"""barnameh benevisid yak rashteh az karbar daryaft konid va tol an ra 
baresi konid agar tol reshteh zoj bod namayash nimeh aval reshte dar gheyre 
in sorat nime akhar chap namayad"""


a=input("yak reshteh vard konid:")
b= len(a)
if b%2==0:
    print(a[ :b//2])
else:
    print(a[b//2: ])