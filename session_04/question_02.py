""" barnameh benevisid az karbar bekhahad yeki az gozine hay sang  kaqhaz va
 qheichi ra vard konid va computer be sort tasadofi entkhab va barandeh elam
konid va agar vorodi qheir se mord bala bod be karbar payam va meqhdar mojadad
vard konid agar karbar exit nevesht ejra bazi khatemeh yabad"""

import random
while True:
    karbar=input("vard konid sang or kaqhaz or qheichi:").strip().lower()
    print(karbar)
    if karbar == "exit":
        print("bazi tamam shod")
        break
    sistem=random.choice(["sang","kaqhaz","qheichi"])
    print( "computer:",sistem)
    if karbar == "sang" and sistem == "kaqhaz":
     print("karbar barandeh shod")
    elif karbar == "kaqhaz" and sistem == "qheichi":
     print("barname barandeh shod")
    elif karbar == "sang" and sistem == "qheichi":
     print("karbar barandeh shod")
    elif karbar == "qheichi" and sistem == "sang":
     print("sistem barandeh shod")
    elif karbar == "qheichi" and sistem == "kaqhaz":
     print("karbar barandeh shod")
    elif karbar == "kaqhaz" and sistem == "sang":
     print("karbar barandeh shod")
    else:
     print("mojadad meqhdar vard konid:")