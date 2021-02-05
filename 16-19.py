
# # exercise 16 ...................................................
# li = input().split(',')
# ans = []
# for i in li:
#     if int(i) % 2 ==1:
#         ans.append(int(i)*int(i))
# ans = [str(i) for i in ans]
# print(','.join(ans))

# # exercise 17 ...................................................
# total = 0
# while True:
#     s = input()
#     if not s:
#         break
#     s = s.split(" ")
#     op = s[0]
#     am = int(s[1])
#     if op == "D":
#         total += am
#     elif op == 'W':
#         total -= am
#     else:
#         pass
# print(total)

# # exercise 18 ...................................................
# import re
# pas = input().split(',')
# ans = []
# for p in pas:
#     cnt = 0
#     cnt += (6<=len(p) and len(p)<=12)
#     # print(cnt)
#     cnt += bool(re.search("[a-z]", p))   # here re module includes a function re.search() which returns the object information
#     # print(cnt)                         # of where the pattern string i is matched with any of the [a-z]/[A-z]/[0=9]/[@#$] characters
#     cnt += bool(re.search("[A-Z]", p))   # if not a single match found then returns NONE which converts to False in boolean
#     # print(cnt)                         # expression otherwise True if found any.
#     cnt += bool(re.search("[0-9]", p))
#     # print(cnt)
#     cnt += bool(re.search("[$#@]", p))
#     # print(cnt)
#
#     if cnt == 5:
#         ans.append(p)
#
# print(','.join(ans))

# # exercise 19 ...................................................
from operator import itemgetter, attrgetter
# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(',')))
#
#
# print(sorted(l, key=itemgetter(0,1,2)))
# # print(sorted(l, key=itemgetter(2)))
# # print(sorted(l, key=attrgetter('name')))       # using attribute  -> https://docs.python.org/3/howto/sorting.html

# another solution

lst = []
while True:
    s = input().split(',')
    if not s[0]:                          # breaks for blank input
        break
    lst.append(tuple(s))

lst.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))  # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
print(lst)