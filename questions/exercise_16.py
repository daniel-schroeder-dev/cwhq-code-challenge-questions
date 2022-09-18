shopping_cart = []
options = """
    What would you like to do?

    1.) Add an item to the shopping cart
    2.) Update an item in the shopping cart
    3.) Remove an item from the shopping cart
    4.) Exit
"""

while True:
    print(f"Here's your current shopping cart: {shopping_cart}")
    user_choice = int(input(options))

    if user_choice == 1:
        item_name = input("What item would you like to add? ")
        shopping_cart.append(item_name)
    elif user_choice == 2:
        index = int(input("What is the index number of the item you want to update? "))
        item_name = input("What is the new item name you want to use? ")
        shopping_cart[index] = item_name
    elif user_choice == 3:
        index = int(input("What is the index number of the item you want to remove? "))
        removed_item = shopping_cart.pop(index)
        print(f"Removed {removed_item} from your shopping cart.")
    elif user_choice == 4:
        print("Goodbye!")
        break

