import time
start = time.time()

num,number,position,product='',1,1,1

while len(num)<=1000000:num+=str(number);number+=1

for x in range(len(num)):
    if x==position-1:product*=int(num[position-1]);position*=10

print(product)

end = time.time()
print(end - start)
