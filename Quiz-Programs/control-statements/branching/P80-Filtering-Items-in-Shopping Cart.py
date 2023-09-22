# Filtering Items in a Shopping Cart
"""
If you have a shopping cart with various items and want to calculate the
total cost, you can use "continue" to skip items that are out of stock
or have special conditions.
"""
total_cart_price = 0
while True:
    user_cart_choice = input("Do you want to add items to cart? Enter 'Yes' or 'No' ")
    if user_cart_choice == 'No':
        print("User don't want to add items to the cart! Quitting the program")
        break
    elif user_cart_choice == 'Yes':
        print("User want to add items to the cart")
        item_name = input("Enter the item name")
        item_price = float(input("Enter the item price"))
        stock_availability = input("item is in the Stock, Enter 'Yes' or 'No' ")
        if stock_availability == 'No':
            print("Item is not available in the stock, will not add this item to cart")
            continue
        elif stock_availability == 'Yes':
            total_cart_price = total_cart_price + item_price
        else:
            print("User has entered the wrong choice, please enter 'Yes' or 'No'")
    else:
        print("User has entered the wrong choice, please enter 'Yes' or 'No'")
print("total cart price = ", total_cart_price)


