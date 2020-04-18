x = 600851475143
a = 1
while x!=1:
    a=a+1
    if x%a == 0:
        while x%a == 0:
            x = x/a
print(a)






