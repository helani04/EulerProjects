import time
x=[]

start = time.time()
for n in range(12,28123):
    b=2
    sum=1
    while b<=n//b:
        if n%b==0:
            if b==n//b:
                sum+=b
            else:
                sum+=(b+n//b)
        if sum>n:
            x.append(n)
            break
        b+=1

sumOfAbundantNo=[]
sum=0
for a in range(len(x)):
    for b in range(a,len(x)):
        if x[a]+x[b]<28123  :
            sumOfAbundantNo.append(x[a]+x[b])


for a in set(sumOfAbundantNo):
    sum+=a
total=0
for c in range(1,28123):
    total+=c
print(total-sum)

end = time.time()
print(end - start)
