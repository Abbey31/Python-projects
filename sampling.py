number = int(input("Enter a number and get the multiplication table"))
count = 1
product = number * count
while count < 20:
    count += 1
    
    print(number,  "X" , count ,  "=",  number*count)
