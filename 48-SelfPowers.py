import time
start = time.time()

sum=0

for i in range(1000): sum+=pow(i+1,i+1)

print(str(sum)[-10:])

end = time.time()
print(end - start)
