# a=int(input("enter range:"))
# for i in range(2,a):
#     prime=True
#     for j in range(2,i):
#         if i % j == 0:
#             prime=False
#             break   
#     if prime:
#         print(i)
for i in range(2,18):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)