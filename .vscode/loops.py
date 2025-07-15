# count = 1
# while count <= 5:
#     print("hello")
#     count += 1
# print(count)

# i = 1
# while i <= 5:
#     print("hello", i)
#     i += 1

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended")

# Q1.
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# Q2.
# i = 100
# while i >= 1:
#     print(i)    
#     i -= 1

# Q3.
# n = int(input("numher:"))
# i = 0
# while i <= 10:
#     print(n*i)
#     i += 1

# Q4.
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(num) :
#     print(num[idx])
#     idx += 1

# heroes = ["spiderman, superman, batman, ironman, hulk"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1

# Q5.
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("number:"))
# idx = 0
# while idx < len(num):
#     if(x == num[idx]):
#         print("found", num[idx])
#     idx += 1


# i = 1
# while i <= 5:
#     print(i)
#     if (i == 3):
#         break
#     i += 1
# print("end of the loop")

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("number:"))
# idx = 0
# while idx < len(num):
#     if(x == num[idx]):
#         print("found", num[idx])
#         break
#     else: 
#         print("finding...")
#     idx += 1

# i = 1
# while i <= 5:
#     if (i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("end of the loop")

# i = 1
# while i <= 10:
#     if (i % 2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("odd no.")    

# i = 1
# while i <= 10:
#     if (i % 2 == 0):
#         print(i)
#         i += 1
#         continue
#     i += 1

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)

# tup = (1, 2, 3, 4, 5, 6)    
# for num in tup:
#     print(num)

# str = "Annapurna"    
# for ch in str:
#     if (ch == "r"):
#         print("found")
#         break
#     print(ch)
# else :
#     print("END") 

# Q6.
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in nums :
#     print(i)
     
# Q7.
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("enter the number :"))
# idx = 0
# for i in tup:
#     if (i == x):
#         print("found")
#     idx += 1    


# seq = range(5)
# print(seq[0])
# print(seq[1])

# seq = range(5)
# for i in seq:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(3, 9 ):  range(start, stop)
#     print(i)

# for i in range(1, 10, 2):  range(start , stop, step)
#     print(i)

# for i in range(2, 11, 2): all even numbers
#     print(i)

# for i in range(1, 10, 2):  all odd numbers
#     print(i)


# Q8.
# for i in range (1, 101):
#     print(i)

# Q9.
# for i in range(100, 0, -1):
#     print(i)

# Q10.
# n = int(input("enter the no.:"))
# for i in range(1, 11):
#     print(n*i)

# for i in range(5):
#     pass
# print("Done")

# n = int(input("enter the number:"))
# sum = 0
# i = 1
# while i <= n :
#     sum += i
#     i += 1
# print("sum:", sum)

# n = int(input("enter a number:"))
# sum = 0
# for i in range(1, n+1):
#     sum += i
#     i += 1
# print("sum :", sum)

# n = int(input("enter a number:"))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
#     i += 1
# print("factorial :", fact)    

