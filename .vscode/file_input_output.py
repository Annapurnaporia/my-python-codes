# f = open("fifth_programe.py", "r")
# data = f.readline()
# print(data)
# print(type(data))
# f.close()

# f = open("firstprogram.py", "r")
# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)
# f.close()

# f = open("firstprogram.py", "r")
# data = f.read()
# print(data)
# f.close()

# f = open("demo.txt", "w")
# f.write("This is a new line added to the file.")

# f = open("demo.txt", "a")
# f.write("\n i want to learn java, c, c++ too")
# f.write("\n then i will become pro")
# f.close()

# f = open("sample.txt", "r")
# data = f.read()
# print(data)
# f.close()
# this will give output as the error as No such file or directory: 'sample.txt'

# f = open("sample.txt", "w")
# f.close()
# f = open("sample_1.txt", "a")
# f.close()
# this will create two new files as sample.txt and sample_1.txt

# f = open("demo.txt", "r+")
# f.write("abc")
# print(f.read())
# f.close()

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("aassssddddddfhkkkkkl;kkk")

# import os
# os.remove("demo.txt")

# with open("practice.txt", "w") as f:
#     f.write("\n Hi everyone")
#     f.write("\n we are learning I/O")
#     f.write("\n using java")
#     f.write("\n I like programming in java")

# with open("practice.txt", "r")as f:
#     data = f.read()    
# new_data = data.replace("java", "python")
# print(new_data)
# with open("practice.txt", "w")as f:
#     f.write(new_data)

# with open("practice.txt", "r")as f:
#     data = f.read()
#     if data.find("learning") != -1:
#         print("found")
#     else :
#         print("not found")    

# def check_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r")as f:
#         while data:
#             data = f.readline()
#             if word in data :
#                 print(line_no)
#             line_no += 1
# check_line()

# def check_even():
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         nums = data.split()
#         for val in nums:
            
        
# check_even()   

