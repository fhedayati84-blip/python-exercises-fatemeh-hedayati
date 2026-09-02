
ramz=input("enter ramz:")
error_count = 0
if len(ramz)<8:
    print("ramz bayad hadahgal 8 karacter bashad")
    error_count +=1
if not any(i.isupper()for i in ramz):
    print("ramz bayad hadahgal yek harf bozorg bashad")
    error_count +=1
if not any(i.islower()for i in ramz):
    print("ramz bayad hadahgal yak harf kochik bashad")
    error_count +=1
if not any(i.isdigit()for i in ramz):
    print("ramz bayad hadahgal yak adad dashte bashad")
    error_count +=1
if not any(i in "!@#$%^&*"for i in ramz):
    print("ramz bayad hadahgal karacter khas bashad ")
    error_count +=1
if error_count>0:
    print("ramz is invalid")  
else:
    print("ramz in valid")
            
    