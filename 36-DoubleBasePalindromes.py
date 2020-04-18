import time
start = time.time()

def checkingPalindromic(n):
    mid=len(n)//2
    if len(n)%2==1:
        if n[:mid]== n[-1:mid:-1]:return True
    elif n[:mid]== n[-1:mid-1:-1]:return True
    else:
        return False

sum=0
for i in range(1000000):
    if checkingPalindromic(str(i)) and checkingPalindromic(str(bin(i))[2:]):sum+=i
print(sum)

end = time.time()
print(end - start)
