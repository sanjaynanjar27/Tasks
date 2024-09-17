# import _re
# import time
# import math
# import pandas as pd
# from numpy.ma.extras import ndenumerate
# from pandas.conftest import names
# from pkg_resources import ensure_directory
# from numpy import  random
# import numpy as np


# # reverse list
# ls = [124,466,77,7445,7435,435,45]
# x = 0
# rev  = []
# for i in range(len(ls)):
#     rev.append(ls[x-1])
#     x = x - 1
# print(rev)

# count = 0
# num = 6
# for i in ls:
#     if num == i:
#         count += 1
# print(f"{num} is repeated {count} times")

# print(sum(ls))
# print(sum(ls)/len(ls))
# total = 0

# lst = {x : x + 1 for x in range(1,10) }
# print(lst)

# non key-word argument
# def data(*args):
#     for i in args:
#         print(i)
# data('hii','good','morning')

# keyword argument
# def data(**kwargs):
#     for key in kwargs:
#         # print("%s = %s" % (key,kwargs[key]))
#         print(key, "=", kwargs[key])
# data(name = "sanjay", age = 23, subject = "Python")

# a = [1,2,3,4,53,46,56,56,]
# b = a[1:3]
# print(b)

# try:
#     a =  10 / 0
# except ZeroDivisionError as e:
#     print(e)


# def a(b):
#     return  lambda d : d * b
# print((lambda x : x * 2)(3))

# Filtering
# ls = [1,4,5,7,8,9,2,1,23,43,44,31]
# fl = list(filter(lambda x : x%2 == 0, ls))
# print(fl)

# Mapping
# ls = [2017,1900,2012,2000]
# a1 = list(map(lambda x : x ** 2,ls))
# print(a1)

# new_line = ord('\n')
# print(new_line)

# txt = 'Good Morning, Hello Google'
# res = re.findall('d',txt)
# print(res)

# res = re.sub("\s","9",txt)
# print(res)

# res = re.findall("^hi",txt)
# if res:
#     print("We Have The Results")
# else:
#     print("Couldn't Find The Match")

# data = list(filter(lambda x : (x % 400 == 0 and x % 100 == 0) or (x%4 == 0 and x%100 != 0),ls))
# print(data)

# Decorators
# def full_name(text):
#     return text.upper()
# def city(text):
#     return text.lower()
# def run(submit):
#     data = submit("Details To Pass through an argument")
#     print(data)
#
# run(full_name)
# run(city)

# def security_code(pin):
#     def bank_balance(amount):
#         if pin == 1234:
#             print(f"Bank Balance is {amount}")
#         else:
#             print(f"{pin} is Incorrect Correct Pin")
#     return bank_balance
#
# d = security_code(12334)
# d(25000)

# Calculating Time taken to find a factorial

# def factorial(fact):
#     def innerData(*args, **kwargs):
#         begin = time.time()
#         fact(*args, **kwargs)
#         end = time.time()
#         print(f"Taken time is : {fact.__name__} , {end - begin}")
#     return  innerData
#
# @factorial
# def count(num):
#     time.sleep(2)
#     print(math.factorial(num))
# count(10)

# Nested Function
# def outer(x):
#     def inner(y):
#         return x+y
#     return inner
# data = outer(5)
# print(data(10))

# Function as Value in Parameter
# def name(val):
#     def data():
#         return  f"Hello {val}"
#     return data
#
# ad = name("MyName")
# print(ad())

# Without annotation
# def decorator_func(fun1):
#     def inner_func():
#         print("It's Decorated function")
#         fun1()
#     return inner_func
#
# def other():
#     print("Other Function")
#
# var = decorator_func(other)
# var()

# Using annotation to decorate function

# def decorator_func(fun1):
#     def inner_func():
#         print("Inner Function Decorated")
#         fun1()
#     return inner_func
#
# @decorator_func
# def other():
#     print("Other FUnction Which is using decorator function annotation ")
# other()

# Using Parameters to decorator
# def division_task(fun1):
#     def inner_funct(a,b):
#         print(f"Division of {a} and {b} ")
#         if b == 0:
#             print("Could not perform Process")
#             return
#         return fun1(a,b)
#     return  inner_funct
#
# @division_task
# def data(a,b):
#     print(a/b)
# data(6,8)

# Chaining Decorators

# def stars(fun1):
#     def inner_funct(*args, **kwargs):
#         print("*" * 15)
#         fun1(*args,**kwargs)
#         print("*" * 15)
#     return  inner_funct
# def mods(fun1):
#     def inner_funct(*args,**kwargs):
#         print("%"*15)
#         fun1(*args,**kwargs)
#         print("%"*15)
#     return  inner_funct
# @mods
# @stars
# def printer(msg):
#     print(msg)

# printer("Good Morning")

# arr = np.array([1,2,4,2,234,3,2,3])
# print(arr)
# print(np.__version__)
# print(type(arr))
#
# # 0D Array
# d0 = np.array(123)
# print(f"Array Dimension {d0.ndim}")
# print(d0)
#
# # 1D Array
# d1 = np.array([12,3,2,5,4],dtype='S')
# print(f"Array Dimension {d1.ndim}")
# print(d1)
#
# # 2D Array
# d2 = np.array([[1,2,3,3],[2,4,5,7]])
# print(f"Array Dimension {d2.ndim}")
# print(d2)
#
# # 3D array
# d3 = np.array([[[1,2,3],[2,3,5],[3,2,3],[21,2,4]]])
# print(f"Array Dimension {d3.ndim}")
# print(d3)
#
# # Declaring Dimension while creating array
# d5 = np.array([1,34,6,7,7],ndmin=4)
# print(d5)
#
#
# # Accessing values
# print(d1[0])
# # first raw third element
# print(d2[0,2])
# # second raw first element
# print(d3[0,1,0])
#
# # Iterate integer as String
# for i in np.nditer(d1, flags=['buffered'], op_dtypes=['S']):
#     print(i)
#
# # iterate in different steps
# for i in np.nditer(d3[:,::2]):
#     print(i)

# for idx , i in ndenumerate(d1):
#     print(idx, i)
# for id , i in ndenumerate(d2):
#     print(id,i)

#Wrong answer in w3 schools

# import numpy as np
# filter_arr = arr > 3
# print(filter_arr)

# arr = np.array([7, 8, 9, 10])
# filter_arr = arr > 9
# newarr = arr[filter_arr]
# print(newarr)

# a = random.randint(123,size=(10))
# print(a)
#
# b = random.rand(5)
# print(b)
#
# c = random.choice([1,2,4])
# print(c)
#
# data = [1,2,4,5,9]
# a = pd.Series(data,index=['a','b','c','d','e'])
# print(a)
#
# calories = {"day1": 420, "day2": 380, "day3": 390}
# d = pd.Series(calories)
# print(d)
#
# calories = {"day1": 420, "day2": 380, "day3": 390}
# data = pd.DataFrame(calories)


# # Inheritance
# class Person(object):
#     def __init__(self,name,e_id):
#         self.name = name
#         self.e_id = e_id
#
#     def display(self):
#         print(f"Name : {self.name}")
#         print(f"Employee Id:  {self.e_id}")
#
#     def details(self):
#         print(f"Name : {self.name}")
#         print(f"Employee Id:  {self.e_id}")
#
# class Employee(Person):
#     def __init__(self,name,e_id,salary,post):
#         self.salary = salary
#         self.post = post
#         Person.__init__(self,name,e_id)
#     def details(self):
#         print(f"Salary : {self.salary}")
#         print(f"Position Id:  {self.post}")
#
# data = Employee("Sanjay",123834,123000,"Intern")
# data.display()
# data.details()
#
#
# # PolyMorphism

# from numpy.distutils.system_info import flame_info


def intro():
    print("Yes Some flies some doesn't")


class Bird:
    def flight(self):
        print("May Be")

class Sperrow(Bird):
    def flight(self):
        print(f"Sparrows Flies")

class Crow(Bird):
    def flight(self):
        print(f"Crows also fly")

data = Bird()
data1 = Sperrow()
data3 = Crow()

data.flight()
intro()

data1.flight()
intro()

data3.flight()
intro()


data4 = Crow()
data4.flight()
intro()