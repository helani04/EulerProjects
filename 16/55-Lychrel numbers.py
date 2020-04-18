
def isPalindrome(n):
    if str(n)==str(n)[-1::-1]:return True
    else :return False
count,y,numbers=0,0,[]
for x in range(10,10000):
    if x in numbers:continue
    y=x+int(str(x)[-1::-1])
    numbers.append(x)
    numbers.append(int(str(x)[-1::-1]))
    for i in range(50):
        z=0
        if (i==0 and isPalindrome(y)) or (i>0 and isPalindrome(z)):break
        numbers.append(y)
        numbers.append(int(str(y)[-1::-1]))
        z=y+int(str(y)[-1::-1])
        print(x,y,z)
        if i==50:count+=1
print(count)
