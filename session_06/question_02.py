inventory={"apple":20,"banana":5,"orange":0,"milk":12,"bread":0}
available=[]
out_of_stock=[]
count=0
count_out_of_stock=0
for i in inventory:
    if inventory[i]>0:
       available.append(i)
       count+=1
    else:
       out_of_stock.append(i)
       count_out_of_stock+=1
print("available:","_"+"\n-".join(available))
print("mojod ast:",count)
print("out_of_stock:","_"+"\n-".join(out_of_stock))
print("mojod nist:",count_out_of_stock)
