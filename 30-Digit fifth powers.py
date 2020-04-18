total=0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        if pow(a,5)+pow(b,5)+pow(c,5)+pow(d,5)+pow(e,5)+pow(f,5)==int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)):
                            total+=int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
                            print(int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)))
print(total-1)
