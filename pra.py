def table():
    for num in range(1,11):
        if num % 2 == 0:
            print(f"Even:{num:^:8}")
        elif num % 2 == 1:
            print(f"Odd:{num:^8}")