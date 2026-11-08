products = {
    "mouse": 1500,
    "keyboard": 3000,
    "monitor": 12000
}

def find_product(products, name):
    if name in products:
        return products[name]
    return None

def change_price(products, name, new_price):
    if name in products:
        products[name] = new_price
        return True
    return False

def remove_product(products, name):
    if name in products:
        products.pop(name)
        return True
    return False

while True:
    print("1. Find product")
    print("2. Change price")
    print("3. Remove product")
    print("4. Shopping cart")
    print("5. Show all products")
    print("6. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        print("You Selected: Find Product")

        name = input("Enter product name: ").lower()
        result =  find_product(products, name)

        if result is not None:
            print("Price:", result)   
        else:
            print("Product not found")

    elif choice == "2":
        print("You selected: Change price")

        name = input("Enter product name: ").lower()
        new_price = int(input("Enter new price: "))
        result = change_price(products, name, new_price)

        if result is True:
            print("New Price:", products[name])
        else:
            print("Target not found")
    
    elif choice == "3":
        print("You selected: Remove Product")
        
        name = input("Enter product name: ").lower()
        result = remove_product(products, name)

        if result is True:
            print("Sucessfully removed", name)
        else:
            print("Target not found")    
    
    elif choice == "4":
        print("You selected: Shopping Cart")

    elif choice == "5":
        print("You selected: Show All products")
    elif choice == "6":
        break
    else:
        print("Invalid Option")