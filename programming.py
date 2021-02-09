
# for _ in range(int(input())):
#     input()
#     arr = list(input().split())
#     print(arr)         #   str

# for _ in range(int(input())):
#     input()
#     arr = [int(x) for x in input().split()]
# #   print(arr)           # int
#     a = arr.count(1)
#     b = arr.count(2)
#     if a % 2==0 and b % 2==0:
#         print('YES')
#     elif b % 2==1 and a % 2==0 and a>=2:
#         print('YES')
#     else:
#         print("NO")

import math
for _ in range(int(input())):
    a,b,m = input().split(' ')
    a=int(a)
    b=int(b)
    m=int(m)
    arr = [int(x) for x in input().split()]
    brr = [int(x) for x in input().split()]

    # print(arr)
    for i in range(m):
        brr[i] = int(math.ceil(brr[i]/a))
    # print(brr)

    for i in range(m):
        tem = arr[i]
        arr[i] = b - arr[i]*brr[i]
        b = b - tem * brr[i]
    # print(arr)

    if( 0 < arr[m-2] or m == 1) :
        print('YES')
    else:
        print('NO')