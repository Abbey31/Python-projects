inventory = {}
cart = {}

def add_new_products():
    product_name = input("Enter the name of the product you want to add:\n ")
    price = float(input("Enter the price of the product: "))
    inventory[product_name] = price
    print(f"{product_name} with {price} added to cart successfully")

def display_items_and_values():
    print("---------YOUR CART-----------")
    if inventory:
        for product_name,price in inventory.items():
            print(f" product:{product_name}| price:{price}",sep='|')

def update_stock_quantities():
    pass

while True:
    user = input("Press 1 to add a product:\npress 2 to display items_and_prices:\nPress 3 to update stock quantities\npress q to quit:")
    if user == "1":
        add_new_products()
    elif user == "2":
        display_items_and_values()
    elif user == "3":
        update_stock_quantities()
    elif user == "q".lower():
        break
    else:
        print("invalid input")

    
    