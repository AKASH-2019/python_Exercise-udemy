# # exercise 26...............................................

# def SumFunction(number1, number2):
# 	return number1 + number2
#
# print(SumFunction(1,2))
#
# # another solution
# sum = lambda n1,n2: n1 + n2
#
# print(sum(1,2))

# # exercise 27...............................................
# def printValue(n):
# 	print(str(n))
#
# printValue(3)
#
# con = lambda x: str(x)
# print(con(3))

# # exercise 28...............................................
# ans = lambda n1,n2: int(n1)+int(n2)
# print(ans("1","5"))

# # exercise 29...............................................
# ans = lambda n1,n2: n1+n2
# print(ans("1","5"))

# # exercise 30...............................................
# def comparelen(s1,s2):
#     if(len(s1) > len(s2)):
#         print(s1)
#     elif(len(s1) < len(s2)):
#         print(s2)
#     else:
#         print(s1+'\n'+s2)
#
#
# comparelen("akash","akash")
# # another sol
# ans = lambda a,b:print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+a)
# ans("akash","akash")

