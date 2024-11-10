# # 
# class Employee:
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'


# emp_1 = Employee('Corey','Schafer',50000)
# emp_2 = Employee('Test','User',60000)

# # print(emp_1)
# # print(emp_2)


# print(emp_1.email)
# print(emp_2.email)
# ENCAPSULATION
# class MyClass(object):
#     def set_val(self, val):
#         self.value = val

#     def get_val(self):
#         return self.value
    
# a = MyClass()
# b = MyClass()

# a.set_val(100)
# b.set_val(100)

# print(a.get_val())
# print(b.get_val())
# class MyInteger(object):
#     def set_val(self, val):
#         try:
#             val = int(val)
#         except ValueError:
#             return 
#         self.val = val 
#     def get_val(self):
#         return self.val
#     def increment_val(self):
#         self.val = self.val + 1
# i = MyInteger()
# i.val = 'hi'
# print (i.increment_val())


# __init__ Method / Constructor
# class MyNum:
#     def __init__(self, value):
#         print("calling __init__")
#         self.val = value

#     def increment(self):
#         self.val += 1

# dd = MyNum(5)
# dd.increment()
# dd.increment()
# print(dd.val)
#Class Attributes vs Instance Attributes
# class YourClass(object):
#     classy = 'class value!'

# dd = YourClass()
# print(dd.classy)

# dd.classy = 'inst value!'

# print(dd.classy)
# del dd.classy
# print(dd.classy)

# class InstanceCounter(object):
#     count = 0

#     def __init__(self,val):
#         self.val = val
#         InstanceCounter.count += 1

#     def set_val(self,newval):
#         self.val = newval

#     def get_val(self):
#         return self.val
    
#     def get_count(self):
#         return InstanceCounter.count
    
# a = InstanceCounter(5)
# b = InstanceCounter(13)
# c = InstanceCounter(17)

# for obj in (a,b,c):
#     print("val of obj: %s" % (obj.get_val()))
#     print("count: %s" % (obj.get_count()))
    
# class MaxSizeList(object):
#     def __init__(self,max):
#         self.max_size = max
#         self.innerlist = []

#     def push(self,obj):
#         self.innerlist.append(obj)
#         if len(self.innerlist) > self.max_size:
#             self.innerlist.pop(0)

#     def get_list(self):
#         return self.innerlist
# a = MaxSizeList(3)
# b = MaxSizeList(1)

# a.push("hey")
# a.push("hi")
# a.push("Let's")
# a.push("go")

# b.push("hey")
# b.push("hi")
# b.push("Let's")
# b.push("go")
# print(a.get_list())
# print(b.get_list())
#INHERITANCE 
# class Date(object):
#     def get_date(self):
#         return '2014-10-13'
    
# class Time(Date):
#     def get_time(self):
#         return '08:13:07'
    
# dt = Date()
# print(dt.get_date())

# tm = Time()
# print(tm.get_time())
# print(tm.get_date())
# class Animal(object):
#     def __init__(self,name):
#         self.name = name
#     def eat(self,food):
#         print('%s is eating %s.' % (self.name,food))

# class Dog(Animal):
#     def fetch(self, thing):
#         print('%s goes after the %s!' % (self.name, thing))

# class Cat(Animal):
#     def swatstring(self):
#         print('%s shreds the string!' % (self.name))

# r = Dog('Rover')
# f = Cat('Fluffy')

# r.fetch('paper')
# f.swatstring()
# r.eat('dog food')
# f.eat('cat food')
# r.swatstring()
#POLYMORPHISM
# class Animal(object):
#     def __init__(self,name):
#         self.name = name

#     def eat(self,food):
#         print('{0} eats {1}'.format(self.name, food))

# class Dog(Animal):

#     def fetch(self, thing):
#         print('{0} goes after the {1}!'.format(self.name,thing))

#     def show_affection(self):
#         print('{0} wags tail'.format(self.name))

# class Cat(Animal):
#     def swatstring(self):
#         print('{0} shreds the string!'.format(self.name))

#     def show_affection(self):
#         print('{0} purrs'.format(self.name))

# for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
#     a.show_affection()
# import random

# class Animal(object):
#     def __init__(self,name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self,name):
#         super(Dog,self).__init__(name)
#         self.breed = random.choice(['Shih Tzu','Beagle','Mutt'])

#     def fetch(self,thing):
#         print('%s goes after the %s!' % (self.name,thing))

# d = Dog('dogname')
# print(d.name)
# print(d.breed) 
# class A(object):
#     def dothis(self):
#         print('doing this in A')

# class B(A):
#     pass
# class C(A):
#     def dothis(self):
#         print('doing this in C')

# class D(B,C):
#     pass
# d_instance = D()
# d_instance.dothis()

# print (D.mro())
#MULTIPLE INHERITANCE
# class InstanceCounter(object):
#     count = 0

#     def __init__(self,val):
#         self.val = val
#         InstanceCounter.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val
#     @cl
#     def get_count(cls):
#         return InstanceCounter.count
    
# a = InstanceCounter(5)
# b = InstanceCounter(13)
# c = InstanceCounter(17)

# for obj in (a,b,c):
#     print("val of obj: %s % (obj.get_val())")
#     print("count: %s" % (obj.get_count()))
import random


class WriteMyStuff(object):
    def __init__(self, writer):
        self.writer = writer

    def write(self):
        write_text = "this is a silly message"
        self.writer.write(write_text)

fh = open('test.txt','w')
w1 = WriteMyStuff(fh) 
w1.write()
fh.close()

w2 = WriteMyStuff(fh)
w2.write()

print('file object:', open('test.txt','r').read())