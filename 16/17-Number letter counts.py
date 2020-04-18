num=1
count=0
three=["1","2","6"]
four=["5","9","4"]
five=["3","7","8"]
n=0
n1=""
for a in range(1,13):
    a=str(a)

    if len(a)==3 :
        if a[0] in three :
            count+=13
        elif a[0] in four :
            count+=14
        elif a[0] in five:
            count+=15
    if len(a)>1:
        if len(a)==2 :
            n=0
        elif len(a)==3:
            n=1
        if a[n] in ["2","3","4","8","9"]:
            count+=6
        elif a[n] in ["5","6"]:
            count+=5
        elif a[n]==1 and a[n+1]==0:
            count+=3
        elif a[n]==7:
            count+=7
    if len(a)==2:
        n1=a
    elif len(a)==3:
        n1=a[1:3]
    if n1 in ["11","12"]:
        count+=6
    elif n1 in ["15","16"]:
        count+=7
    elif n1 in ["13","14","18","19"]:
        count+=8
    elif n1=="17":
        count+=9
    elif len(a)==1:
        n=0
    elif len(a)==3:
        n=2
    elif len(a)==2 and a[0]!=1:
        n=1
    if a[n] in three :
        count+=3
    elif a[n] in four :
        count+=4
    elif a[n] in five:
            count+=5
    print(count)
print(count)



