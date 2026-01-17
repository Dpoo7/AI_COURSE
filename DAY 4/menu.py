products = ["1.chai","2.coffee","3. Water","4.exit"]

for product in products 
    print(product)

selected_pro=int(input("Select product:"))

if selected_pro == 1:
    print("chai")

elif selected_pro == 2:
    print("coffee")

elif selected_pro == 3:
    print("Water")

else:
    print("Nothing Else")