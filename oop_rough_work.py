# class Employee:
#     pass
#     def __init__(self, first,last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

# emp_1 = Employee('Corey','Schafer',50000)
# emp_2 = Employee('Test','User',60000)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())

from car import Car

car1 = Car("Mustang",2024,"red",False)
car2 = Car("Corvette",2025,"blue",True)
car3 = Car("Charger",2026,"yellow",True)

car1.drive()
car1.stop()

car2.drive()
car2.stop()

car3.drive()
car3.stop()