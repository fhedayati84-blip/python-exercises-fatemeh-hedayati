a1=input("jomleh1 ra vard konid:")
a2=input("jomleh2 ra vard konid:")
kalamat=a1.lower().split()
kalamat2=a2.lower().split()
kalame_moshtarak = []
for i in kalamat:
    if i in kalamat2 and i not in kalame_moshtarak:
      kalame_moshtarak.append(i)
print("kalame moshtarak")
for i in kalame_moshtarak:
    print(i)
    
            
