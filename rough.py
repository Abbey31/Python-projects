# FUNCTIONS
# def main():
#     x = int(input("What's x? "))
#     print("x squared is", square(x))

# def square(n):
#     return pow(n,2)

# main()
# passing the return value of a previous function to another function
# def main():
#     x = int(input("What's x? "))
#     print("x squared is",square(x))

# def square(n):
#     return n * n
# main()
#SIMILARLY
# def main():
#     x = int(input("What's x? "))
#     print("x squared is",square(x))

# def square(n):
#     return pow(n,2)
# main()
# LIST COPREHENSION
# fruits = ["apples","bananas","strawberries"]
# new_fruits = []
# for fruit in fruits:
#     fruit = fruit.upper()
#     new_fruits.append(fruit)

#     fruits = new_fruits
#     print(fruits)
fruits = ["apples","bananas","strawberries"]
fruits = [fruit.upper() for fruit in fruits]

print(fruits)