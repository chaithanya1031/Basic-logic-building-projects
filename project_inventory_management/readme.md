🧾 Inventory Management System (Python)
📌 Overview

This is a simple console-based inventory management program written in Python.
It allows users to purchase items, update stock levels, and automatically handle stock depletion.

The system ensures:

Only valid items can be purchased

Users can’t buy more than what’s in stock

Inventory updates dynamically

Program exits when user types "exit" or when all items run out of stock

⚙️ Features

✅ View and purchase available items (pen, book, eraser)
✅ Prevents invalid item names
✅ Prevents purchasing quantities greater than available stock
✅ Auto-updates inventory after each purchase
✅ Detects when items are out of stock
✅ Automatically stops when all stock is sold
✅ Simple text-based interface for quick testing and learning

💻 Code Explanation
1. Initialize Inventory
inventory = {'pen': 10, 'book': 5, 'eraser': 12}


Each item starts with a predefined quantity.

2. Continuous Purchase Loop
while True:


Runs indefinitely until the user types 'exit' or all stock is sold.

3. Ask for Item
ask = input('what do you want(pen,book,eraser): ')


User inputs an item name or 'exit' to leave.

4. Exit Condition
if ask == 'exit':
    print('Exiting the system..')
    break


Cleanly exits the loop.

5. Validate Item
if ask not in inventory:
    print('Invalid item. Please choose from pen, book or eraser')
    continue


Prevents typing errors or unavailable items.

6. Ask Quantity and Validate
quantity = int(input(f'How many {ask} do you want: '))
if quantity > inventory[ask]:
    print(f'sorry, only {inventory[ask]} {ask} left in stock')
    continue


Ensures users don’t overbuy beyond available stock.

7. Update Inventory
inventory[ask] -= quantity
print(f'{quantity} {ask}(s) purchased successfully!')


Reduces stock count after each successful purchase.

8. Handle Out-of-Stock Items
if inventory[ask] == 0:
    print(f'{ask.capitalize()} is now out of stock')


Notifies when a specific item runs out.

9. End Program When All Items Are Sold
if all(qty == 0 for qty in inventory.values()):
    print('All items are out of stock. Closing the store')
    break


Program automatically closes when everything is sold out.

🧠 Example Run
what do you want(pen,book,eraser): pen
How many pen do you want: 3
3 pen(s) purchased successfully!

what do you want(pen,book,eraser): book
How many book do you want: 2
2 book(s) purchased successfully!

what do you want(pen,book,eraser): exit
Exiting the system..

🧩 Possible Improvements

Add option to restock items

Store inventory data in a JSON file (persistent storage)

Add prices and calculate total bill

Handle invalid numeric inputs safely using try-except

Include admin mode to update inventory

📜 License

This project is open-source and free to use for educational purposes.