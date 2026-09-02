brnameh = input()
f=brnameh.split()
if not f:
    print("جمله خالی است")
else:
    counts={}
    for i in f:
     if i in counts:
         counts[i] +=1
     else:
         counts[i]=1
         max_i=""
         max_count=0
         for i in counts:
              count=counts[i]
              if count>max_count:
               max_count=count
               max_i=i
    if max_count == 1:
              print("هیچ کلمه ای بیش از یک بار تکرار نشده ")
    else:
              print(f"{max_i}{max_count}")