import math
import time
start = time.time()
total=0
for a in range(100,math.factorial(9)):
    num=str(a)
    sum=0
    for b in num:
        sum+=math.factorial(int(b))
        if sum>a or '9'in num :
            break
    if sum==a:
        total+=a
print(total)
end = time.time()
print(end - start)
