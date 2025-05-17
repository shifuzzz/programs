for i in range(1,5):
    for j in range(1,i+1):
        if j==1:
            print("*",end=" ")
        elif j==i:
            print("*",end=" ")
        elif i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")  
    print()
