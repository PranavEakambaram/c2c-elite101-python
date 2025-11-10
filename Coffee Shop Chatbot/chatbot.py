from order_menu import menu
from make_your_own_coffee import bases, milks, sugars, drizzles

cart = []

print("Welcome to Pranav's Coffee Shop!")
user_name = input ("What's your name?")
user_age = input("How old are you?")
print(f"Hi {user_name}! How can I help you today?")


while True:
    print("Please select one of the following options.")
    print("1. Order a Coffee")
    print("2. Build Your Own Coffee")
    print("3. View Your Cart / Checkout")
    print("4. Leave Feedback")
    print("5. Exit")

    choice = input("What would you like to do?")

    if choice == "1":

        print("Here's Our Menu:")
        print("")
        for i in menu:
            print(i['product_id'] + ": " + i['Name'] + " - " + i['Price'])

        product_id = input("Enter the product ID of the drink you would like to add to cart. Enter 'Quit' to go back.")

        if product_id == "Quit":
            pass

        else:
            item = None
            for i in menu:
                if i['product_id'] == product_id:
                    item = i
                    break

            if item:
                cart.append(item)
                print("Item has been added to cart!")
            else:
                print("Product not found")






    elif choice == "2":
        print("Choose your base:")
        for b in bases:
            print("hi")





    elif choice == "3":
        if len(cart) == 0:
            print("Your Cart is Empty. Enter 'Quit' to go back.")
        else:
            print("Here's Your Cart:")

            for i in cart:
                print(i['product_id'] + ": " + i['Name'] + " - " + i['Price'])

            action = input("Enter a product ID to remove an item, or enter 'Checkout' to purchase, or enter 'Quit' to go back")

            if action == "Checkout":
                print ("Your coffee will be ready in 5 minutes")

            elif action == "Quit":
                pass

            else:
                item = None
                for i in cart:
                    if i['product_id'] == action:
                        item = i
                        break

                if item:
                    cart.remove(item)
                    print("Item has been removed from your cart!")
                else:
                    print("Product not found")




    elif choice == "4":
        asdf





    elif choice == "5":
        print(f"Thank you, {user_name}, Hope to see you again!")
        break
    else:
        print("That's not an option. Please enter a number 1-5.")
