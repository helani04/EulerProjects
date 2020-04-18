n=0
n1=1000
count=0
while count<500:
    n=(n1*n1+n1)/2
    f=1
    count=0
    while f<=n/2:
        if n%f==0:
            count+=1
        f+=1
    n1+=1
    print(n)
print(n)
C:\Users\helan\Desktop\ProjectEuler\
