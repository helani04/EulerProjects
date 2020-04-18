a=2
s=0
while a<2000000:
    b=2
    while a%b!=0 and a/2>b:
        b=b+1
    if a==b:
        s=s+a
        print(s)
    a=a+1
print(s)

