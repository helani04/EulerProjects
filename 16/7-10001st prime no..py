i=1
p=2
while i<10000:
   p=p+1
   a=2
   while a<p & p%a!=0 :
       a=a+1
   if a== p-1:
       i=i+1
print(p)

