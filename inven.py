inventory = {}  # To hold available products and their prices  
cart = {}       # To hold items selected by the customer  

# Function to add a product to the inventory  
def add_product():  
    product_name = input("Enter the name of the product: ")  
    price = float(input("Enter the price of the product: "))  
    inventory[product_name] = price  
    print(f"Added {product_name} with price {price} to inventory.")  

# Function to update stock quantities (if you plan to track quantities)  
def update_stock_quantities(product_name, quantity):  
    # You can store quantities in another dictionary if needed.  
    pass  # For now, let's keep this simple  

# Function to display items and values in inventory  
def display_items_and_values():  
    if inventory:  
        print("Available products:")  
        for product, price in inventory.items():  
            print(f"{product}: ${price:.2f}")  
    else:  
        print("No products available in inventory.")  

# Function to add a product to the cart  
def add_to_cart():  
    product_name = input("Enter the name of the product you want to add to the cart: ")  
    if product_name in inventory:  
        quantity = int(input("Enter the quantity: "))  
        if product_name in cart:  
            cart[product_name] += quantity  # Update quantity if already in cart  
        else:  
            cart[product_name] = quantity  # Add new product to cart  
        print(f"Added {quantity} of {product_name} to cart.")  
    else:  
        print("Product not found in inventory.")  

# Function to display cart items and their total value  
def display_cart():  
    if cart:  
        total = 0.0  
        print("Your cart:")  
        for product, quantity in cart.items():  
            price = inventory[product]  
            subtotal = price * quantity  
            print(f"{product}: {quantity} x ${price:.2f} = ${subtotal:.2f}")  
            total += subtotal  
        print(f"Total: ${total:.2f}")  
    else:  
        print("Your cart is empty.")  

# Example usage  
def main():  
    while True:  
        print("\nOptions:")  
        print("1. Add Product")  
        print("2. Display Inventory")  
        print("3. Add to Cart")  
        print("4. Display Cart")  
        print("5. Exit")  
        
        choice = input("Choose an option (1-5): ")  
        if choice == '1':  
            add_product()  
        elif choice == '2':  
            display_items_and_values()  
        elif choice == '3':  
            add_to_cart()  
        elif choice == '4':  
            display_cart()  
        elif choice == '5':  
            print("Exiting the program.")  
            break  
        else:  
            print("Invalid choice. Please try again.")  

# Run the program  
main() 

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
        print("#" * width)
        
main()