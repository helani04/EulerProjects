import time
start = time.time()

i = 286
while i>=286:
    m=i*(i+1)/2
    if (1+pow(1+24*m,1/2))%6==0 :
        if (1+pow(1+8*m,1/2))%4==0:print(m);break
    i+=1

end = time.time()
print(end - start)
