import time
start = time.time()
year=1901
day=6
firsts=1
count=0
while year<=2000:
    if year%400==0 or (year%4==0 and year%100!=0):
        feb=29
    else:
        feb=28
    months=0
    NoOfDaysInMonths=[31,feb,31,30,31,30,31,31,30,31,30,31]
    while months<12:
        if day==firsts:
            count+=1
        if day-firsts>7:
            firsts+=NoOfDaysInMonths[months]
            months+=1
        day+=7
    year+=1
print(count)
end = time.time()
print(end - start)
