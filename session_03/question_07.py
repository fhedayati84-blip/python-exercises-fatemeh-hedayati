"""barnameh benevisid se rang az vorodi begirad agar do rang yeksan chap do
 rang yeksan agar se rang yeksan chap namayad  se rang yeksan ast dar gheir
 in sort agar yeksan nabodand chap shavad yeksan nist"""


color1=input("رنگ اول را وارد کنید:")
color2=input("رنگ دوم را وارد کنید:")
color3=input("رنگ سوم را وارد کنید:")
if color1==color2==color3:
    print("سه رنگ یکسان هست")
elif color1==color2 or color1==color3 or color2==color3:
    print("دو رنگ یکسان است")
else:
    print("رنگ یکسان نیست")
