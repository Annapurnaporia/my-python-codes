# making a class
# class Car:

#     # default constructors
#     def __init__(self):
#         pass

#     # parameterized constructors
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#         print("making a new car...")

# # making an object
# car_1 = Car("BMW", "black")    
# print(car_1.name, car_1.color) 

# car_2 = Car("mercedes", "blue")
# print(car_2.name, car_2.color)

# attribute
# class student:
#     # class attribute (common attribute). only gets to store one time in the memory
#     # class.attr(e.g : student.collage_name)
#     collage_name = "ABIT"
#     # collage_name is common attribute for every student
#     name = "anynomous"
#     def __init__(self,name,marks):
#         # object attribute. gets to store multiple times in the memory becouse of change in values.
#         # object.attr(e.g : s1.name)
#         # object attribute precedence value is greater then class attribute(object atrr > class atrr)
#         self.name = name
#         self.marks = marks

# s1 = student("Annap", "99") 
# # s1 is an object and name, marks are atrributes
# print(s1.name, s1.marks)

# s2 = student(student.name, 98)
# print(s2.name, s2.marks)

# print(student.collage_name)
        

# class student:
#     # class is acollection of attributes and methods
#     collage_name = "ABIT"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     # here method is defined
#     # welcome() is a method name 
#     # self is a ompulsory parameter
#     # the functions that we creat in the class is known as mehods

#     def welcome (self):
#         print("welcome student", self.name)
#     def get_marks (self):
#         return self.marks

# s1 = student("Annap", 99)
# # object.methode_name is a way to call method
# s1.welcome()
# print(s1.get_marks())

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def Avg(self) :
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print("average :", sum/3)
            
    
# s1 = student("Annap", [96, 97, 99])
# print(s1.name )
# s1.Avg()

# static method
# class student():
#     def __init__(self):
#         pass

#     # @staticmethod is a decorater which convertes normal method to a static method
#     # method which does not use self parameter and works at a class level is known as static method
#     @staticmethod
#     def hello ():
#         print("Hello")
# student.hello()

# oops : abstraction, encapsulation, inheritance, polymorphism
# abstraction
# abstraction hides unnecessary details of a class and shows only the essential feature to the user 
# class Car :
#     def __init__(self):
#         self.acc = False
#         self.clutch = False
#         self.brk = False

#     def car_started(self):
#         self.acc =True
#         self.clutch =True
#         print("Car started...")

# c_1 = Car()
# c_1.car_started()

# encapsulatin 
# encapsulation is wrapping the data and function in a single unit

# class Account :
#     def __init__(self, balane, account_no):
#         self.balance = balane
#         self.account_no = account_no

#     # debit method
#     def debit (self, amount):
#         self.balance -= amount
#         print("rs.", amount , "was debited")
#         print("total amount :", self.get_balance())

#     def credit (self, amount):
#         self.balance += amount
#         print(f"rs. {amount} was credited")
#         print("total amount :", self.get_balance())


#     def get_balance (self):
#         return self.balance

# acc_1 = Account(5000000, 123345645365874685)  
# acc_1.debit(100)      
# print(acc_1.get_balance())


# class student :
#     def __init__(self, name):
#         self.name = name

# s1 = student("Annap")
# print(s1.name)
# del keyword used to delete the object property or object itself
# del s1.name 
# print(s1.name) this will show error as  'student' object has no attribute 'name'


# private 
# private attributes and methodes are meant to be used only inside the class, they are not accessible outside the class
# class Account :
#     def __init__(self, __acc_pass, __acc_no) :
#         self.__acc_pass = __acc_pass
#         self.__acc_no = __acc_no

#     def reset_password(self):
#         # we can access this inside the class
#         print(self.__acc_pass)
#         print(self.__acc_no)

# acc_1 = Account("anmncnsjcnm ", 1234568)
# # we can access information outside the class only by calling the method
# acc_1.reset_password()
# print(acc_1.__acc_pass)
# print(acc_1.__acc_no)
# above statement will give error as 'Account' object has no attribute '__acc_pass'
# becouse acc_pass and acc_no are private information which will only acceseble in a class
# we can create a private attribute by adding "__" befor the attribute (e.g --> __acc_pass, __acc_no)

# class person :
#     __name = "anynomus"

#     def __hello(self,__name) :
#         self.__name  = __name
#         print("hello ",self.__name)

#     def welcome(self):
#         print("Welcome !")
#         self.__hello("Annapurna")

# p1 = person()
# p1.welcome()

# inheritance : i. single inheritance ii. multilevel inheritance iii. multiple inheritance
# single inheritance : one child class derived from one parent class
# parent class
# class Car :
#     @staticmethod
#     def starts() :
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")
# child class
# class Toyotacar(Car) :
#     def __init__(self,name):
#         self.name = name

# c1 = Toyotacar("innova")
# print(c1.starts)

# multilevel inheritance : 
# it has one main/parent/base class and from it multiple child classes are derived
# class Car:
#     @staticmethod
#     def started ():
#         print("car started...")

#     @staticmethod
#     def stoped():
#         print("car stoped")

# class Mercedes(Car):
#     def __init__(self, price) :
#         self.price = price

# class Benz(Mercedes):
#     def __init__(self, engine):
#         self.engine = engine

# c1 = Mercedes("4.20 cr.")
# print(f"it's price is {c1.price}")
# c1 = Benz(1500)
# print(f"it has {c1.engine}cc engine")
# c1.started()

# multiple inheritance :
# one derived/child class inherites attributes of multiple main/parent class
# class A:
#     varA = "Welcome! to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome! to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

# super method
# used to access the methodes of parent class
# class Car :
#     def __init__(self,name):
#         self.name = name

#     @staticmethod
#     def starts() :
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class Toyotacar(Car) :
#     def __init__(self, type, name):
#         super().__init__(name)
#         self.type = type
#         super().starts()

# c1 = Toyotacar("disel", "innova")
# print(f"{c1.name} is a {c1.type} car")

# class method
# class method is bound to the class and recieves the class as a implicit first argument
# static method can not access or modify class state generally used for utility
# class person:
#     name = "anynomus"

#     def changename (self, name):
        # normally their are two methods to access the attributes of class thorough the method of class(indirect call) as given bellow :
        # person.name = name
        # self.__class__.name = "Annap"

# p1 = person()
# p1.changename("Annapurna")
# print(p1.name)
# print(person.name)

# class person:
#     name = "anynomus"

        # to call directly in the function
    # @classmethod (decorator)
    # in classmethod we take cls as the parameter 
#     def changename (cls, name):
#         cls.name = name

# p1 = person()
# p1.changename("Annapurna")
# print(p1.name)
# print(person.name)


# without using property decorator

# class student :
#     def __init__(self, physics, chemistry, math) :
#         self.physics = physics
#         self.chemistry = chemistry
#         self.math = math
#         self.percentage =  str((self.math + self.physics + self.chemistry) / 3) + "%"

#     def cal_percentage(self):
#         return str((self.math + self.physics + self.chemistry) / 3) + "%"

# s1 = student(97, 98, 99)
# print(s1.percentage)

# s1.physics = 99
# print(s1.physics)
# s1.cal_percentage()
# print(s1.cal_percentage())

# property decorator
# we use @property decorater on any method in the class to use method as a property

# class student :
#     def __init__(self, physics, chemistry, math) :
#         self.physics = physics
#         self.chemistry = chemistry
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.math + self.physics + self.chemistry) / 3) + "%"

# s1 = student(97, 98, 99)
# print(s1.percentage)

# s1.physics = 99
# print(s1.percentage)

# polymorphism : operter overloading
# when the same is allowed to operater have different meaning according to the context

# print(1 + 2) #3
# print("anna" + "purna") #concatinate
# print([1, 2, 3] + [3, 4, 5]) #merge

# class complex :
#     def __init__(self, real, img) :
#         self.real = real
#         self.img = img

#     def showNumber(self) :
#         print(f"{self.real} i + {self.img} j")

#     def __add__ (self, num2) : # dunder function __add__ = addition
#         new_real = num1.real + num2.real
#         new_img = num1.img + num2.img
#         return complex(new_real,new_img)
    
#     def __sub__ (self, num2) : # dunder function __sub__ = substraction
#         new_real = num1.real - num2.real
#         new_img = num1.img - num2.img
#         return complex(new_real,new_img)
    
#     def __mul__ (self, num2) : # dunder function __mul__ = multiplication
#         new_real = num1.real * num2.real
#         new_img = num1.img * num2.img
#         return complex(new_real,new_img)

#     def __truediv__ (self, num2) : # dunder function __truediv__ = division
#         new_real = num1.real / num2.real
#         new_img = num1.img / num2.img
#         return complex(new_real,new_img)
    
#     def __mod__ (self, num2) : # dunder function __mod__ = modulus
#         new_real = num1.real % num2.real
#         new_img = num1.img % num2.img
#         return complex(new_real,new_img)

# num1 = complex(2, 3)
# num1.showNumber()
# num2 = complex(3, 4)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()

# num4 = num1 - num2
# num4.showNumber()

# num4 = num1 * num2
# num4.showNumber()

# num4 = num1 / num2
# num4.showNumber()

# num4 = num1 % num2
# num4.showNumber()

# class circle :
#     def __init__(self, radius) :
#         self.radius = radius

#     def area (self):
#         return self.radius ** 2
    
#     def perimeter (self):
#         return 2 * (3.14) * (self.radius)
    
# c1 = circle(23)
# print(c1.area())
# print(c1.perimeter())

# class employee :
#     def __init__( self, role, department, salary) :
#         self.role = role
#         self.department = department
#         self.slary = salary
    
#     def showDetails (self) :
#         print(f" role : {self.role} \n department : {self.department} \n salary : {self.slary}")

# class engineer(employee) :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Ethicalhacker", "security", 70000)

# E1 = engineer("Annapurna", 20)
# E1.showDetails()

# class Order :
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, ord2):
#         return self.price > ord2.price
    
# ord1 = Order("book", 90)
# ord2 = Order("pen", 10)
# print(ord1 < ord2)