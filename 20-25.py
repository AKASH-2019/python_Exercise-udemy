# exercise 20...............................................
# class gen:
#     def mul_seven(self,n):
#         for i in range(0,int(n/7)+2):
#             yield i*7
#
# ob = gen()
# for i in ob.mul_seven(int(input())):
#     print(i)

# # exercise 21...............................................
# import math
#
# x,y = 0,0
# while True:
#     s = input()
#     if not s:
#         break
#     s = s.split(" ")
#     if s[0]=="UP":
#         x+=int(s[1])
#     if s[0]=="DOWN":
#         x-=int(s[1])
#     if s[0]=="RIGHT":
#         y+=int(s[1])
#     if s[0]=="LEFT":
#         y-=int(s[1])
#
# print(round(math.sqrt(x**2 + y**2)))

# # exercise 22...............................................
# s = input().split()
# dic = {}
#
# for i in s:
#     dic.setdefault(i,s.count(i))
# # # dic = sorted(dic.keys())
# # # dic = sorted(dic.items())
# dic = sorted(dic.items())
# # print(dic)
# for i in dic:
#     print(f'{i[0]}:{i[1]}')

# # exercise 23...............................................
# n = int(input())
# print(n**2)

# # exercise 24...............................................
# import square as square
#
# print(f'sorted: {sorted.__doc__}')
# print(f'power: {pow.__doc__}')
# print(f'square: {square.__doc__}')

# # exercise 25...............................................

# class Person:
#     # Define the class parameter "name"
#     name = "Person"
#
#     def __init__(self, name = None):
#         # self.name is the instance parameter
#         self.name = name
#
# jeffrey = Person("Jeffrey")
# print(Person.name, jeffrey.name)
#
# nico = Person()
# nico.name = "Nico"
# print(Person.name, nico.name)

