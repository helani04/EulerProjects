n=1
check = True
c=2
p=2
import math
while c<=20:
    b=1
    a=2
    while c%a != 0:
        a=a+1
    if c==a:
        p=c
        if check:
           if p<=math.sqrt(20):
              b=math.floor(math.log10(20)/math.log10(p))
           else:
              check=False
        print(p,b)
        n=n*(p**b)
    c=c+1
print(n)












