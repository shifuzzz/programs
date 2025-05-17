even=0
odd=0
n=int(input("enter no of elements:"))
print("enter the no's:")
for i in range(n):
    a=int(input())
    if a % 2 == 0:
        even=even+1
    else:
        odd=odd+1
print("total even no's=",even)
print("total odd no's=",odd)