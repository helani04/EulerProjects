n=20
m=11
while m<=20:
    n=n+1
    while n%m==0:
        m=m+1
        if m==21:
            print(n)
            break
    if n%m!=0:
        m=11






