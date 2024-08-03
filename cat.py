#i = 3
#while i != 0:
 #   print("meow") 
  #  i -= 1
    # another way
#i = 1
#while i <= 3:
 #   print("meow")
  #  i += 1

#INFINITE LOOP
#while True:
 #   n = int(input("What's n? "))
  #  if n > 0:
   #     break

#for _ in range(n):
 #   print("meow")
  #loop with function
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what's n?"))
        if n > 0:
            break
        return n

def meow(n): 
    for _ in range(n):
        print("meow") 

main() 