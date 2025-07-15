# function defination
# def arithmatic_operation(a, b):  function parameters
#     sum = a + b
#     sub = a - b
#     mul = a * b
#     div = a/b
#     return sum, sub, mul, div
# print(arithmatic_operation(10, 5))  function call ; arguments

# def print_hello ():
#      print("Hello")
# print_hello()
# print_hello()

# output = print_hello()
# print(output)  None

# avg of 3 nums.

# def avg (a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg
# print(avg(10, 30, 40))
# print(avg(3, 4, 5))

# print("annapurna", end=" ")  
# print("poria")

# def product(a, b=1):  
#     print(a*b)
#     return a*b
# product(3)

# Q1.
# def length_list(list):
#     return (len(list))
# print(length_list([1, 2, 3, 4, 5]))
# print(length_list([1, 2, 3, 4, 5, 6, 7]))

# movies = ["avengers", "rush hour", "catch me if you can"]
# print(length_list(movies))

# Q2.
# def el_list(list):
#     for i in list:
#         print (i, end =" ")
# el_list([1, 2, 3, 4, 5])
# el_list([3, 5, 7, 9])

# Q3.
# n = int(input("enter :"))
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return (fact)
# print(factorial(n))

# n = int(input("enter :"))
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#         print (fact)
# factorial(n)
# output enter :4
# 1
# 2
# 6
# 24

# Q4.
# n = int(input("USD :"))
# def currecy_converter(n):
#     INR = n * 86
#     return INR
# print(currecy_converter(n))

# Q5.
# n = int(input("Enter :"))
# def check_even(n):
#     if n % 2 == 0:
#         return "Even"
#     else :
#         return "Odd"
# print(check_even(n))

# def show(n):
#     if (n == 0):
#         return
#     print(n, end = " ")
#     show(n - 1) 
# show(5)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else :
#         return n * factorial(n - 1)
# print(factorial(5))

# def sum (n):
#     if n == 0:
#         return 0
#     else :
#         return n + sum(n - 1)
# print(sum(5))    

# def el_list(list, index = 0):
#     if len(list) == index:
#         return
#     else :
#         print(list, index + 1)
# el_list([1, 2, 3, 4,5])

def welcome(name):
    print("welcome", name)
welcome("Annapurna")    