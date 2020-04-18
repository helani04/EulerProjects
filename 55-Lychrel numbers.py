import time
start = time.time()

def isPalindrome(n):
    if str(n)==str(n)[-1::-1]:return True
    else :return False
count,y=0,0
for x in range(10000):
    y=x+int(str(x)[-1::-1])
    for i in range(51):
        if isPalindrome(y):break
        y=y+int(str(y)[-1::-1])
        if i==50:count+=1
print(count)

end = time.time()
print(end - start)
