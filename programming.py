
# for _ in range(int(input())):
#     input()
#     arr = list(input().split())
#     print(arr)         #   str

for _ in range(int(input())):
    input()
    arr = [int(x) for x in input().split()]
#   print(arr)           # int
    a = arr.count(1)
    b = arr.count(2)
    if a % 2==0 and b % 2==0:
        print('YES')
    elif b % 2==1 and a % 2==0 and a>=2:
        print('YES')
    else:
        print("NO")