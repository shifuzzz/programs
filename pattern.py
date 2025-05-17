# for i in range(5,0,-1):
#     for j in range(6):
#         if j>=i:
#             print("*",end=" ")
#         else:       
#             print(" ",end=" ")  
#     print()


a=float(input("enter 1st side:" ))
b=float(input("enter 2nd side:" ))
c=float(input("enter 3rd side:" ))

sides=sorted([a,b,c])
if sides[0]**2+sides[1]**2==sides[2]**2:
    print("right traiangle")
else:
    print("not right triangle")




for i in range(0,26):
    for j in range(i):
        print(chr(j+65),end=" ")
    print()








