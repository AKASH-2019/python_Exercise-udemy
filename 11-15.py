
# exercise 11 ...................................................
# input: 0100,0011,1010,1001
# seq = [x for x in input().split(",")]
# ans = []
# for v in seq:
#     d = int(v,2)
#     if d % 5 == 0:
#         ans.append(v)
# print(','.join(ans))
#
# # another way............................
# def div5(x):
#     reversed(x)
#     total, pw = 0, 1
#
#     for i in x:
#         total+= (ord(i)-48) * pw                #   ord() print the ascii value
#         pw*=2
#     if total % 5 == 0:
#         return True
#
# seq = [x for x in input().split(",")]
# ans = []
# for x in seq:
#     if div5(x):
#         ans.append(x)
# print(','.join(ans))

# # exercise 12 ...................................................
# ans = []
#
# for i in range(1000,3001):
#     flag = 0
#     for j in str(i):
#         if ord(j) % 2 != 0:
#             flag=1
#             break
#
#     if flag == 0:
#         ans.append(str(i))
# print(','.join(ans))

# # exercise 13 ...................................................
# s = input()
# cs, cd = 0, 0
# for i in s:
#     if (i >='a' and 'z' >= i) or (i >= 'A' and i <= 'Z'):
#         cs+=1
#     elif ((i>='0' and i<='9')):
#         cd+=1
# print(f'LETTERS {cs} \nDIGITS {cd}')

# # another solution
# s = input()
# d = {"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])

# # exercise 14 ...................................................

# s = input()
# Upper = sum(1 for i in s if i.isupper())
# Lower = sum(1 for i in s if i.islower())
#
# print(f'UPPER CASE {Upper}')
# print(f'LOWER CASE {Lower}')

# # exercise 15 ...................................................
v = input()
total,tem= 0,str()
for i in range(4):
    tem+=v
    total+=int(tem)

print(total)
