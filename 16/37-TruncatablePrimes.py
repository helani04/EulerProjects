import math
import time
start = time.time()
def isPrime(a):
    b=2
    while a%b!=0 and b<a//b :b=b+1
    if a==1 or a==6:return False
    elif b-1==round(math.sqrt(a)) or b==round(math.sqrt(a)) and  b!=math.sqrt(a) :return True
    else:return False

count,number,sum=0,23,0
while count<11:
    if isPrime(number):
        num=str(number)
        for i in range(1,len(num)):
            if isPrime(int(num[i:])) and isPrime(int(num[:len(str(number))-i])):
                if i==len(num)-1:count+=1;sum+=number
            else:break
    number+=2
print(sum)

end = time.time()
print(end - start)
