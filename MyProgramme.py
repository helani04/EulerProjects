for row in range(6):
    for col in range(9):
        if col==4:
            print(" *",end="")
        else:
            print("  ",end="")
    print()
for row in range(8,15):
    for col in range(9):
        if(row-col==10 or (col==0 and (row==9 or row==10)) or(col==8 and(row==9 or row==10)) or (row==8 and (col==1 or col==2 or col==6 or col==7)) or (row==9 and(col==3 or col==5)) or (col==4 and row==10)or (row==11 and col==7) or (row==12 and col==6) or (row==13 and col==5)):
            print(" *",end="")
        else:
            print("  ",end="")

    print()
for row in range(15,21):
    for col in range(9):
        if(col==1 or col==6 or(row-col==14) ):
            print(" *",end="")
        else:
            print("  ",end="")

    print()


