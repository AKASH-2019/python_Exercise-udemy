
# exercise 1...............................

# data = range(2000, 3201)
#
# for value in data:
#     if value % 7 ==0 and value % 5 != 0:
#         print(value, end=',')

# # 2nd way
# print(*(i for i in range(2000,3201)), sep=',')

# # exercise 2..................................
#
# def fac(n):
#     if n == 0:
#         return 1
#     return n * fac(n-1)
#
# print(fac(int(input())))

# exercise 3..................................
# n = int(input())

# d = dict()
# for i in range(1,n+1):
#     d[i]= i * i
#
# print(d)

# # 2nd way
# n = int(input())
# d = dict()
# d = {i : i *i for i in range(1,n+1)}
# print(d)

# # exercise 4 .............................................
# data = input().split(",")
# t = tuple(data)
# print(data)
# print(t)

# # exercise 5 .............................................

# class Input_Output_Str:
#     def get_str(self):
#         self.s = input()
#     def print_str(self):
#         print(self.s.upper())
#
# obj = Input_Output_Str()
# obj.get_str()
# obj.print_str()
