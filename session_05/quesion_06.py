brnameh= input().lower()
kalamat = ["hack","fraud","scam","password","attack"]
counts = {}
for i in kalamat:
    count = 0
    while True:
        index = brnameh.find(i,count)
        if index == -1:
            break
        if i in counts:
            counts[i] +=1
        else:
            counts[i] =1     
        count = index + len(i)
for i,c in counts.items():
     print(f"{i} > {c}")