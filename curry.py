class Customer:
    def __init__(self,name,membership_type):
        self.name = name
        self.membership_type = membership_type
        

c = Customer("Caleb", "Gold")
print(c.name, c.membership_type)
c2 = Customer("Brad","bronze")
print(c2.name,c2.membership_type)

print(c[1].name)
