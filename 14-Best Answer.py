def counting(a):
    count=1
    while a>1:
        if a%2==0:
            a/=2
            count+=1
        else:
            a=a*3+1
            count+=1
    return(count)
numbers=[]
terms=[]
for n in range(500000,1000000):
    numbers.append(n)
    if n%2==0:
        terms.append(counting(n/2)+1)
    else:
        terms.append(counting((3*n+1)/2)+2)
print(numbers[terms.index(max(terms))])
