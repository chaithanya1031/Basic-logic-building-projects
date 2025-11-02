# #inventory management
inventory = {'pen': 10, 'book': 5, 'eraser': 12}
while True:
    ask=input('what do you want(pen,book,eraser): ')
    if ask=='exit':
        print('Existing the system..')
        break
    if ask not in inventory:
        print('Invalid item. Please choose from pen,book or eraser')
        continue
    quantity=int(input(f'How many {ask} do you want: '))
    if quantity>inventory[ask]:
        print(f'sorry,only {inventory[ask]} {ask} left in stock')
        continue
    inventory[ask] -= quantity
    print(f'{quantity} {ask}(s) purchased successfully!')
    if inventory[ask]==0:
        print(f'{ask.capitalize()} is now out of stock')
    if all(qty==0 for qty in inventory.values()):
            print('All times are out of stock. Closing the store')
            break