from order_menu import menu
from make_your_own_coffee import bases, flavors, milks, sugars, drizzles

cart = []
feedback_list = []

print("\n\nWelcome to Pranav's Coffee Shop!")
user_name = input ("\nWhat's your name?")
user_age = input("\nHow old are you?")
print(f"\n\nHi {user_name}! How can I help you today?\n")


while True:
    print("\n\n\nPlease select one of the following options.")
    print("1. Order a Coffee")
    print("2. Build Your Own Coffee")
    print("3. View Your Cart / Checkout")
    print("4. Leave Feedback")
    print("5. Exit")

    choice = input("\nWhat would you like to do?")

    if choice == "1":

        print("")
        print("Here's Our Menu:")
        print("")
        for i in menu:
            print(i['product_id'] + ": " + i['Name'] + " - " + i['Price'])

        product_id = input("\nEnter the product ID of the drink you would like to add to cart. Enter 'Quit' to go back.")

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
                print("\nItem has been added to cart!")
            else:
                print("\nProduct not found")


    elif choice == "2":

        base_selected = None
        while (base_selected == None):
            print("\nChoose your base:\n")

            for b in bases:
                print(b['id'] + ": " + b['Name'])

            base_choice = input ("\nEnter the ID of the base you would like.")

            for b in bases:
                if b['id'] == base_choice:
                    base_selected = b['Name']
                    break

            if base_selected == None:
                print("\nPlease enter a valid base ID\n")
        print(f"\nYour Base: {base_selected}")

        flavor_selected = None
        while (flavor_selected == None):
            print("\nChoose your flavor\n")

            for f in flavors:
                print(f['id'] + ": " + f['Name'])

            flavor_choice = input ("\nEnter the ID of the flavor you would like.")

            for f in flavors:
                if f['id'] == flavor_choice:
                    flavor_selected = f['Name']
                    break

            if flavor_selected == None:
                print("\nPlease enter a valid flavor ID")
        print(f"\nYour Flavor: {flavor_selected}")

        milk_selected = None
        while (milk_selected == None):
            print("\nChoose your milk type:\n")

            for m in milks:
                print(m['id'] + ": " + m['Name'])

            milk_choice = input ("\nEnter the ID of the milk you would like.")

            for m in milks:
                if m['id'] == milk_choice:
                    milk_selected = m['Name']
                    break

            if milk_selected == None:
                print("\nPlease enter a valid milk ID")
        print(f"\nYour Milk: {milk_selected}")

        sugar_selected = None
        while (sugar_selected == None):
            print("\nChoose your sugar level:\n")

            for s in sugars:
                print(s['id'] + ": " + s['Name'])

            sugar_choice = input ("\nEnter the ID of the sugar level you would like.")

            for s in sugars:
                if s['id'] == sugar_choice:
                    sugar_selected = s['Name']
                    break

            if sugar_selected == None:
                print("\nPlease enter a valid Sugar Level ID")
        print(f"\nYour Sugar Level: {sugar_selected}")

        drizzle_selected = None
        while (drizzle_selected == None):
            print("\nChoose your drizzle: \n")

            for d in drizzles:
                print(d['id'] + ": " + d['Name'])

            drizzle_choice = input ("\nEnter the ID of the drizzle you would like.")

            for d in drizzles:
                if d['id'] == drizzle_choice:
                    drizzle_selected = d['Name']
                    break

            if drizzle_selected == None:
                print("\nPlease enter a valid drizzle ID")
        print(f"\nYour Drizzle: {drizzle_selected}")

        print("\n\nYour Coffee: ")
        print(f"Base: {base_selected}\nFlavor: {flavor_selected}\nMilk: {milk_selected}\nSugar: {sugar_selected}\nDrizzle: {drizzle_selected}")


        add_to_cart = input("\nWould you like to add your coffee to your cart? Please answer 'Yes' or 'No'")

        if (add_to_cart == "Yes"):
            custom_coffee = {
                "product_id" : str(len(cart) + 1),
                "Name" : f"Custom Coffee: Base: {base_selected}\nFlavor: {flavor_selected}\nMilk: {milk_selected}\nSugar: {sugar_selected}\nDrizzle: {drizzle_selected}",
                "Price" : "$6.99"
            }
            cart.append(custom_coffee)
            print("\nYour Coffee was added to cart!")

        elif (add_to_cart == "No"):
            print("\nOrder cancelled")



    elif choice == "3":
        if len(cart) == 0:
            print("\nYour Cart is Empty. Enter 'Quit' to go back.")
        else:
            print("\nHere's Your Cart:\n")

            for i in cart:
                print(i['product_id'] + ": " + i['Name'] + " - " + i['Price'] + "\n")

            action = input("\nEnter a product ID to remove an item, or enter 'Checkout' to purchase, or enter 'Quit' to go back.")

            if action == "Checkout":
                print ("\nYour coffee will be ready in 5 minutes")

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
                    print("\nItem has been removed from your cart!")
                else:
                    print("\nProduct not found")




    elif choice == "4":
        print("\nPlease tell us how we can improve!")

        while True:
            print("Please choose one of the following: ")
            print("1. Leave new feedback")
            print("2. View previous feedback")
            print("3. Exit")

            user_ip = input("\nPlease enter '1', '2', or '3'")

            if (user_ip == "1"):
                rating = input("\nRate your experience (1-10): ")
                comment = input("\nPlease leave a mesasge telling us how we can improve")
                print("\nWe greatly appreciate your feedback!")

                feedback ={
                    "rating" : rating,
                    "comment" : comment,
                            }

                feedback_list.append(feedback)

            elif (user_ip == "2"):
                if len(feedback_list)==0:
                    print("\nThere is no feedback yet.")
                else:
                    print("\nCustomer Feedback\n")
                    for i in feedback_list:
                        print(f"\nRating: {i['rating']}/10\nComment: {i['comment']}\n")

            elif (user_ip == "3"):
                break
            else:
                print("\nInvalid choice. Please pick between 1-3")


    elif choice == "5":
        print(f"\nThank you {user_name}, Hope to see you again!")
        break
    else:
        print("\nThat's not an option. Please enter a number 1-5.")
