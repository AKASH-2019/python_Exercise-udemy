# exercise 6 .............................................
import math

# data = input().split(',')
# # print(data)
# # items = [x for x in input().split(',')]
# # print(items)
#
# c = 50
# h = 30
# value = []
# for d in data:
#     value.append(str(int(math.sqrt((2*c*float(d))/h))))
# print(','.join(value))

# # exercise 7 .............................................
# x,y = map(int,input().split(','))
# # print(x,y)
# ans = []
# for r in range(x):
#     temp = []
#     for c in range(y):
#         temp.append(r*c)
#     ans.append(temp)
#
# print(ans)

# # exercise 8 .............................................

# data = input().split(',')
# #  print(sorted(data))
# data.sort()
# print(','.join(data))

# # exercise 9 .............................................

# def soln():
#     while True:
#         x = input()
#         if x:
#             yield x.upper()
#         else:
#             return
#
# for line in soln():
#     print(line)

# # for line in map(str.upper, soln()):
# #     print(line)

# # exercise 10 ....................................................
# #  input-  hello world and practice makes perfect and hello world again
# word = input().split()
# word.sort()
# print(word)
# for w in word:
#     if word.count(w)>=2:
#         word.remove(w)
# print(' '.join(word))

# # #  another way.........
# print(" ".join(sorted(list(set(word)))))

# # #  another way.........
# [word.remove(i) for i in word if word.count(i)>1]
# word.sort()
# print(' '.join(word))






