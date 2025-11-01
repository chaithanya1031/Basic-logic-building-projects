#update prices
items={'apple':100,
       'banana':40,
       'cherry':60,
        }
updated_prices={}
for key,value in items.items():
    updated_prices[key]=value*1.10
print(updated_prices)