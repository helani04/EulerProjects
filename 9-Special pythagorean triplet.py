a=1
while a<=(1000-3)/3 :
    b=a+1
    while b<(1000-3)/2:
        c=1000-a-b
        if c*c==b*b+a*a :
                print(a*b*c)
                print(a,b,c)
        b=b+1
    a=a+1

