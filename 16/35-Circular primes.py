import math
import time
start = time.time()
def isPrime(a):
    b=2
    while a%b!=0 and b<a//b:
        b=b+1
    if b-1==round(math.sqrt(a)) or b==round(math.sqrt(a)) and  b!=math.sqrt(a) :
        return True
    else:
        return False
totCount=0
for a in range(101,1000000,2):
    num=str(a)
    for digit in num:
        if digit in ['0','2','4','6','8','5']:
            condition=False
            break
        else:
            condition=True
    count=0
    if condition:
        if isPrime(a):
            count=1
        for c in range(len(num)-1):
            num1=num
            num=num1[1:]+num1[0]
            if isPrime(int(num)):
                count+=1
        if count==len(num):
            totCount+=1
print(totCount+13)
end = time.time()
print(end - start)
