# class Circle:
#     pi = 3.14
#     def __init__(self, diameter):
#         self.radius = diameter / 2

#     def circumference(self):
#         return 2 * self.pi * self.radius
# pizza = Circle(12)
# print(pizza.circumference())

# class Student:
#     def __init__(self,roll,marks):
#         self.roll = roll
#         self.marks = marks
#     def display(self):
#         print('Roll:', self.roll,'Marks:',self.marks, end=" ")

# student1 = Student(34,'A')
# student1.age = 17
# print(student1.display(), 'Age:',student1.age)

# class Student:
#   # Class variable
#   subject_name = 'Math for Machine Learning'

#   # constructor
#   def __init__(self, name, roll_no):
#     self.name = name
#     self.roll_no = roll_no

# # outside the class
# # create Objects
# s1 = Student('Emma', 10) 
# Student.subject_name = 'Machine Learning'

# print(s1.name, s1.roll_no, s1.subject_name)

# class solution:
#   def initial(self,sets):
#     return self.final(sets)
 
#   def final(self, sets):
#     return list(map(lambda x: ((x**3)%2==0,x**3),sets))

# print(solution().initial([4,5,6]))


class B:
   def two(self):
       return 'B'
class A(B):
   def one(self):
       return self.two()
   def two(self):
       return 'A'   
obj= A()
print(obj.one())