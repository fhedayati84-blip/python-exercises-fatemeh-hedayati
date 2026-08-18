"""barnameh benevisid va mablaq kharid az carbar begirid agar balay yek milyon
toman bod 15 darsad takhfif, bein 500 hezar ta 1 milyon 10 darsad takhfif,
va kamtar az an bedon takhfifi lahaz shavad mablaq nahayi chap konid"""

s=int(input('مبلغ خرید :'))
if s>1000000:
    a=s-(s*0.15)
    print(a)
elif 500000<s<1000000:
    a=s-(s*0.1)
    print(a)
else:
  print(s)
  