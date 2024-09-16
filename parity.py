# x = int(input("What's X?"))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# using function
#def main():
 #   x = int(input("What's x?"))
  #  if is_even(x):
   #     print("Even")
    #else:
     #   print("Odd")
#def is_even(n):
 #   if n % 2 == 0:
  #      return True
   # else:
    #    return False
#main()
# another way
 #x = int(input("What's X?"))

 #if x % 2 == 0:
  #   print("Even")
 #else:
  #   print("Odd")
# shorter way of using function
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    return True if n % 2 == 0 else False
main()