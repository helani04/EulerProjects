b=100
c=0
d=0
while b<1000:
    a=100
    while a<1000:
        c=b*a
        if c<100000:
            if(c//10000 == c%10) and (c%10000)//1000 == (c%100)//10:
                if c>d:
                    d=c
        else:
            if c//100000 == c%10 and (c%100000)//10000 == (c%100)//10 and (c//1000)%10 == (c%1000)//100:
                if c>d:
                    d=c
        a=a+1
    b=b+1
print(d)









