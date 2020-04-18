import time
def sumOfProperDivisors(n):
    a=2
    sum=1
    while a<=n//a:
        if n%a==0:
            if a==n//a:
                sum+=a
            else:
                sum+=(a+n//a)
        a+=1
    return(sum)

start = time.time()

total=0
for a in range(2,10000):
    n1=sumOfProperDivisors(a)
    if a==sumOfProperDivisors(n1) and a!=n1:
        total+=(a+n1)
print(total/2)

end = time.time()
print(end - start)
