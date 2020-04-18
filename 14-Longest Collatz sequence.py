n=500000
number=[]
terms=[]
while n<1000000:
    count=1
    a=n
    while a>1:
        if a%2==0:
            a/=2
            count+=1
        else:
            a=a*3+1
            count+=1
    terms.append(count)
    number.append(n)
    n+=1

print(number[terms.index(max(terms))])
