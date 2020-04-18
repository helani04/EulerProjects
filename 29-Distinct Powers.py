x=[]
for a in range(2,101):
    for b in range(2,101):
        x.append(pow(a,b))
y=set(x)
print(len(y))
