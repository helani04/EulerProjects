n=1
b=1
count=2
while n>0:
    a=n
    n=b
    b=a+n
    count+=1
    if len(str(b))==1000:
        print(count)
        break
