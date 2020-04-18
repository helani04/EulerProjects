a=0
b=1
c=2
d=0
while d<4000000:
    d=b+c
    b=c
    c=d
    if d%2==0:
        a=a+d
print(a+2)





