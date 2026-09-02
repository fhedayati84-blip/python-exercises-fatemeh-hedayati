jomleh=input()
a=jomleh.split()
max_word=a[0]
for i in a:
    if len(i)>len(max_word):
        max_word=i
print(max_word)
print("kalame",len(max_word))
    