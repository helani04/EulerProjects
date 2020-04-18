paths=1
pathsSum=0
for x in range(20):
    paths=1
    for y in range(20):
        if x<19 and y<19:
            paths*=2
        pathsSum+=paths
print(pathsSum)
