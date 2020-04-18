print(1/974)
repeatingCount,remainders=0,[]
for d in range(999,6,-1):
    remainders=[]
    num1=1%d
    while num1 not in remainders:
        remainders.append(num1)
        num1%=d
