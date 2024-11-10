# def multiply(number1,number2):
#     return number1 * number2
# x = multiply(100,10)
# print(x) 
#ARGS
# def add(*all):
#     sum = 0
#     for i in all:
#         sum += i   
#     return sum

# print(add(1,2,3,4,5,6,))
#KWARGS

def hello(**kwargs):
    print("Hello" + kwargs['first']+ " "+ kwargs['last'])