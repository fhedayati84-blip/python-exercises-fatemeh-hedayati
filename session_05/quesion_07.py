brnameh=input()
result=""
count=1
if not brnameh:
    print("")
else:
    for i in range(1,len(brnameh)):
        if brnameh[i] == brnameh[i-1]:
            count += 1
        else:
            result += brnameh[i-1] + str(count)
            count=1
    result += brnameh[-1] + str(count)
    print(result)