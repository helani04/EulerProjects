n=1
c=2
sum=1
while n<1002001:
    for a in range(4):
        n+=c
        sum+=n
    c+=2
print(sum)
