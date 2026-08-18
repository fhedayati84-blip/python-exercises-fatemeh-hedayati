""" barnameh benevisid masafat ti shode az carbar begirid agr masafat kamtar az
2 kilometr bod keraye sabet 20000 toman bashad dar qeir in sorat be ezaye har 
kilometr ezafe 5000 toman kerayeh ezafe shavad keraye nahayi ra chap 
namayid"""
s=int(input('مسافت بر حسب کیلومتر:'))
if s<2:
    print('20000')
else:
    a=20000+((s-2)*5000)
    print(a)