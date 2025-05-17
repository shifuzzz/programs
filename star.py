for i in range(1,5):
    for j in range(1,i+1):
        if j==1:
            print(i,end=" ")
        elif j==i:
            print(i,end=" ")
        elif i==4:
            print(i,end=" ")
        else:
            print(" ",end=" ")  
    print()
