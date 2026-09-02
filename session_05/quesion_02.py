brnameh=input("enter string:").strip()
s=""
for i in brnameh:
    if i not in s:
        s +=i
print(s)