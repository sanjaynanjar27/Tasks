# # import re
# # from itertools import count
# # from random import Random
# # from string import digits
# # from xml.sax import parse


# # # 1) program to find factorial using recursion
# # def find_factorial(n):
# #     if n == 0:
# #         return  1
# #     else:
# #         return n * find_factorial(n-1)
# # print(find_factorial(5))

# # # 2) program to check Armstrong Number
# # digits = int(input("Enter Size Of Digits"))
# # num = int(input("Enter Range Of Your series"))
# # total = 0
# # data = []
# # if count(num) == digits:
# #     for i in str(num):
# #         data.append(int(i) ** digits)
# #     print(sum(data))
# #     print(data)
# #     if sum(data) == num:
# #         print("Armstrong Number
# #     else:
# #         print("Not Armstrong Number")
# # else:
# #      print("Enter Your selected digits")


# # ls= [2]
# # st = int(input('Enter Yur Starting point'))
# # ep = int(input('Enter Yur Ending point'))
# # for i in range(st,ep):
# #     for j in range(2,i):
# #         if (i % j) != 0:
# #             ls.append(i)
# #         break
# # print(ls)

# # program to print Fibonacci sequence
# # a = 0
# # b = 1
# # total = 0
# # num = int(input("Enter Range Of Your series"))
# # print(a, b)
# # for i in range(2, num):
# #     total = a + b
# #     a = b = total
# #     print(total,  end=" ")

# # # 5) program to check if number is palindrome or not
# # num1 = int(input("Enter Number TO Check"))
# # st = ''
# # num2 = num1
# # for i in str(num1):
# #     st = i + st
# # print(st)
# # if int(st) == num2:
# #     print("Number Is Palindrome")
# # else:
# #     print("Number Is Not Palindrome")

# # # 6) program to check if a number is even or odd
# # num = int(input("Enter A Number"))
# # if num > 1:
# #     if num % 2 == 0:
# #         print("Number Is Even")
# #     else:
# #         print("Number Is Odd")
# # else:
# #     print("Enter Valid Number")

# # 7) python program to access global variable in class
# # class Demo():
# #     a = 10
# #     def data(self):
# #         print("This is function.")
# #         a = 20
# #         print(f"variable inside function : {a}")
# # obj = Demo()
# # obj.data()
# # print(f"Global Variable a : {obj.a}")

# # 8) python program to draw a pattern
# # print(""" 1
# #  3 2
# #  6 5 4
# # 10 9 8 7"""
# # )
# # x = 1
# # for i in range(1, 6):
# #     if i > 1:
# #         for j in range(2,i):
# #             if i % 2 == 0:
# #                 print(i,end='')
# #         print('')

# # a = 0
# # for i in range(10):
# #     for x in range(i+1):
# #         print(i * x,end=' ')
# #     print(" ")

# # # # 9) python program to draw a pattern
# # x = 1
# # for i in range(1, 6):
# #     for j in range(1, i):
# #         print(j, end=' ')
# #     for k in range(2, i):
# #         print(x, end=' ')
# #         x += 1
# #     print()

# # # 10) python program to draw a pattern
# # for i in range(1, 10):
# #     for k in range(1):
# #         print(0, end=' ')
# #     for j in range(1, i):
# #         print(i * j, end=' ')
# #     print(" ")

# # # FOmd unique values fro,  this list'
# # size = int(input("Enter A Series Highest : "))
# # data = []
# # dup= []
# # print('Enter Values')
# # for i in range(1, size+1):
# #     a = int(input())
# #     if a > 0:
# #         if a not in data:
# #             data.append(a)
# #         else:
# #             dup.append(a)
# #     for i in dup:
# #         if i in dup:
# #             data.remove(i)
# #             for j in data:
# #                 print(f"Unique Value : {j}")
# #     print(data)

# # # compare the triplets
# # name1 = [5, 6, 8]
# # name2 = [3, 9, 7]
# # for i in range(len(name1)):
# #     if name1[i] > name2[i]:
# #         print(1, end=' ')
# #     elif name1[i] == name2[i]:
# #         print(end=' ')
# #     else:
# #         print(1, end=' ')

# # # # Most common character
# # # # Using comprehension
# # count = 1
# # word = input('Enter Letters')
# # cd = {}
# # d = {x : word.count(x) for x in set(word)}

# # # Using Loop
# # for i in word:
# #     if i in cd:
# #         cd[i] += 1
# #     else:
# #         cd[i] = 1
# # print(cd)
# # for key,  val in cd.items():
# #     print(key,  val)

# # 11. Python program to extract only the numbers from a lst which have some specific digits using Using filter() + lambda
# # Input : test_list = [3456,  23,  128,  235,  982],  dig_list = [2,  3,  5,  4]
# # Output : [23,  235]
# # test_list = [3456,  23,  128,  235,  982]
# # dig_list = [2,  3,  5,  4]
# # ls = []
# # for i in test_list:
# #     for j in dig_list:
# #         if str(j) in str(i):
# #             ls.append(i)
# #         break
# # print(ls)


# # Kangaroo Problem
# # k1 = int(input("Enter First Kangaroo Position."))
# # v1 = int(input("Enter First Kangaroo Steps."))
# # k2 = int(input("Enter Second Kangaroo Position."))
# # v2 = int(input("Enter second Kangaroo Steps."))
# # if k1 > k2 and v1 > v2:
# #     print("No")
# # if k1 < k2 and v1 < v2:
# #     print("No")
# # if v1 == v2:
# #     print("No")
# # if (k2 - k1) % (v1 - v2) == 0:
# #     print("Yes")
# # else:
# #     print("No")

# # n = int(input("Enter How Many Emails You want to validate"))
# # print("Enter Email Address.")
# # check = r'\b[A-za-z0-9._%+-]+@[A-Z, a-z0-9.-]+\.[A-Z|a-z]{2, 7}\b'
# # data = []
# # for i in range(n):
# #     e = input("")
# #     if (e != " ") and (10 <= len(e) <= 80) and (re.fullmatch(check,  e)):
# #              data.append(e)
# #     else:
# #             print(f" {e} Is Not Valid,  Enter Valid Email")
# # print(data)
# # for mails in sorted(data):
# #     print(mails)

# # Word Order
# # n = int(input("Enter Number"))
# # dic = {}
# # words = []
# # for i in range(n):
# #     word = input("")
# #     words.append(word)
# #     if word in dic:
# #         dic[word] += 1
# #     else:
# #         dic[word] = 1
# # print(len(dic))
# # print(dic)

# # if __name__ == '__main__':
# #     total = 0
# #     n = int(input())
# #     student_marks = {}
# #     for _ in range(n):
# #         name,  *line = input().split()
# #         scores = list(map(float,  line))
# #         student_marks[name] = scores
# #     query_name = input()
# #     for i in student_marks[query_name]:
# #         total += i
# #     div = len(student_marks[query_name])
# #     print(format(total/div, '.2f'))

# # ____________________________________________________________________________________________________


# if __name__ == '__main__':
#     t = int(input("Enter number of test cases: "))
#     if 0 < t < 21:
#         data = []
#         for _ in range(t):
#             a_size = int(input())
#             n1 = input().split()
#             b_size = int(input())
#             n2 = input().split()
#             data.append({'A': n1,  'B': n2})
            

#     for i in data:
#             for k in i:
#                 print(i[k])

# # if __name__ == '__main__':
# #     N = int(input())
# #     data=[]
# #     for i in range(N):
# #         query = input("").lower().split(" ")
# #         if 'insert' in query:
# #             data.insert(int(query[1]),int(query[2]))
# #         elif 'append' in query:
# #             data.append(int(query[1]))
# #         elif 'remove' in query:
# #             data.remove(int(query[1]))
# #         elif 'sort' in query:
# #             data.sort()
# #         elif 'reverse' in query:
# #             data.reverse()
# #         elif 'pop' in query:
# #             data.pop()
# #         elif 'print' in query:
# #             print(data)
# #         else:
# #             print("Enter Valid Query")


# rows = int(input("Enter Size of your square pyramid"))

# # Top Triangle
# for i in range(rows):
#     for j in range(1, rows - i + rows): # Putting Space To the top Part
#         print(" ", end=' ')
#     for j in range(2 * i+1): # Printing Top
#         print("T ", end='')
#     print(' ')

# # This is upper half
# for i in range(1, rows):
#     for j in range(rows - i):  # Space before left part
#         print(" ", end=' ')
#     for k in range(i): # This is right part but only half
#         print("R", end=' ')
#     for j in range(1,rows*2): # This is Upper half square
#         print(" ",end=" ")
#     for j in range(i): #Left part of Upper Half
#         print("L",end=' ')
#     print()

# for i in range(rows,0,-1):
#     for j in range(rows-i): # Space before Lower Right part
#         print(" ",end=' ')
#     for k in range(i): # Bottom Right part
#         print("R",end=' ')
#     for j in range(1,rows*2):
#         print(" ",end=" ")  #Bottom Square
#     for j in range(i ):
#         print("L",end=" ") # Bottom LEft Part
#     print()

# # Bottom
# for i in range(rows,0, -1):
#         for k in range(1, rows - i+rows+1):
#             print(" ", end=' ')
#         for k in range(2 * i - 1):
#             print("B", end=' ')
#         print(" ")


