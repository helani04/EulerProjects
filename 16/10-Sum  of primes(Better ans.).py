import math
a=3
sum=2
while a<2000000:
    b=2
    while a%b!=0 and b<a//b:
        b=b+1
    if b-1==round(math.sqrt(a)) or b==round(math.sqrt(a)) and  b!=math.sqrt(a) :
        print(a)
        sum+=a
    a=a+2
print(sum)
