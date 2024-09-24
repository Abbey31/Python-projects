sum_odd_digits = 0
sum_even_digits = 0
total = 0

#step1
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]


# STEP2
for x in card_number[::2]:
    sum_odd_digits += int(x)

#STEP3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

#STEP4
total = sum_odd_digits + sum_even_digits

#STEP5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")