import sys
print("Hello I am FoodBot, welcome to Fire n' Fusion. Please choose your item in each category.")
print("When I ask for your choices enter the code of the menu item.")
menuname= str(input("What is the name you would like your order placed under:"))
questioninput= int(input("Would like to eat here or would you like your order to-go? Enter 1 for eating here and 2 if you would like your meal to-go:"))
if questioninput < 1 or questioninput > 2:
	sys.exit("Sorry there was an error in your input. Please retry!")
print("Here are the appetizers...")
print("-------------------------------")
print("Honey Chilli Potatoes($3.20) - Use Code 1")
print("Paneer Lettuce Wraps($5.10) - Use Code 2")
print("Mini Chicken Tamales($3.55) - Use Code 3 ")
print("Fiery Chicken Meatballs($5.99) - Use Code 4")
print("Enter 5 for Nothing")
appetizerinput = int(input("Enter what you would like in APPETIZERS[Code = 1-5]: "))
if appetizerinput == 1:
	item_price_app = 3.20
elif appetizerinput == 2:
	item_price_app = 5.10
elif appetizerinput == 3:
	item_price_app = 3.55
elif appetizerinput == 4:
	item_price_app = 5.99
elif appetizerinput == 5:
	item_price_app = 0.00
elif appetizerinput < 1 or appetizerinput > 5:
    sys.exit("Sorry there was an error in your input. Please retry!")
print("Here are the Entrees...")
print("-------------------------------")
print("Gobi Munchurian($7.21) - Use Code 6")
print("Grilled Veggie Skewers($5.33) - Use Code 7")
print("Paneer Kathi Rolls($7.79) - Use Code 8")
print("Lemon and Ginger Chicken($8.60) - Use Code 9")
print("Hot Chicken Lasagna($6.45) - Use Code 10")
print("Prisha's Favorite Chicken n'Cheese Enchiladas ($7.84) - Use Code 11")
print("Enter 12 for Nothing")
entreeinput = int(input("Enter what you would like in ENTREES [Code 6-12]:"))
if entreeinput == 6:
	item_price_ent = 7.21
elif entreeinput == 7:
	item_price_ent = 5.33
elif entreeinput == 8:
	item_price_ent = 7.79
elif entreeinput == 9:
	item_price_ent = 8.60
elif entreeinput == 10:
	item_price_ent = 6.45
elif entreeinput == 11:
	item_price_ent = 7.84
elif entreeinput == 12:
	item_price_ent = 0.00
elif entreeinput < 6 or entreeinput > 12:
    sys.exit("Sorry there was an error in your input. Please retry!")
print("Here are the Choices for Bread and Rice...")
print("-------------------------------")
print("Cumin Rice($2.25) - Use Code 13")
print("Egg Friedrice($3.25) - Use Code 14")
print("Plain Kulcha($1.50) - Use Code 15")
print("AlooKulcha($2.25) - Use Code 16")
print("Enter 17 for Nothing")
breadandriceinput = int(input("Enter what you would like in BREAD AND RICE [Code 13-17]:"))
if breadandriceinput == 13:
	item_price_brice = 2.25
elif breadandriceinput == 14:
	item_price_brice = 3.25
elif breadandriceinput == 15:
	item_price_brice = 1.50
elif breadandriceinput == 16:
	item_price_brice = 2.25
elif breadandriceinput == 17:
	item_price_brice = 0.00
elif breadandriceinput < 13 or breadandriceinput > 17:
    sys.exit("Sorry there was an error in your input. Please retry!")
print("Here are the Choices for Desserts...")
print("-------------------------------")
print("Arabic King-Sweets($3.99) - Use Code 18")
print("Coconut Fried IceCream($2.50) - Use Code 19")
print("Supreme Vanilla Fudge($3.75) - Use Code 20")
print("Enter 21 for Nothing")
dessertinput = int(input("Enter what you would like in DESSERTS [Code 18-21]:"))
if dessertinput == 18:
	item_price_des = 3.99
elif dessertinput == 19:
	item_price_des = 2.50
elif dessertinput == 20:
	item_price_des = 3.75
elif dessertinput == 21:
	item_price_des = 0.00
elif dessertinput < 18 or dessertinput > 21:
    sys.exit("Sorry there was an error in your input. Please retry!")
print("Here are the Choices for Drinks...")
print("-------------------------------")
print("Chai($1.00) - Use Code 22")
print("Cookies n' Cream Milkshake($2.50) - Use Code 23")
print("Bottle of Water($1.25) - Use Code 24")
print("FountainDrink($1.50) - Use Code 25")
print("Enter 26 for Nothing")
drinkinput = int(input("Enter what you would like in DRINKS [Code 22-26]:"))
if drinkinput == 22:
	item_price_dri = 1.00
elif drinkinput == 23:
	item_price_dri = 2.50
elif drinkinput == 24:
	item_price_dri = 1.25
elif drinkinput == 25:
	item_price_dri = 1.50
elif drinkinput == 26:
	item_price_dri = 0.00
elif drinkinput < 22 or drinkinput > 26:
    sys.exit("Sorry there was an error in your input. Please retry!")
sauceinput = str(input("Would you like a sauce platter with your meal(enter Yes or No)FREE!:"))
print("                          ")
print("                          ")
print("                          ")
print("                          ")
print("    -----Fire n' Fusion------")
if questioninput == 1:
	print("Meal:EATING IN THE RESTARAUNT")
elif questioninput == 2:
	print("Meal:TO-GO ORDER")
if appetizerinput == 1:
	print("Honey Chilli Potatoes: " + "    $3.20")
elif appetizerinput == 2:
	print("Paneer Lettuce Wraps: " + "     $5.10")
elif appetizerinput == 3:
	print("Mini Chicken Tamales: " + "     $3.55")
elif appetizerinput == 4:
	print("Fiery Chicken Meatballs: " + "  $5.99")
if entreeinput == 6: 
	print("Gobi Munchurian: " + "          $7.21")
elif entreeinput == 7:
	print("Grilled Veggie Skewers: " + "   $5.33")
elif entreeinput == 8:
	print("Paneer Kathi Rolls: " + "       $7.79")
elif entreeinput == 9:
	print("Lemon and Ginger Chicken: " + " $8.60")
elif entreeinput == 10:
	print("Hot Chicken Lasagna: " + "      $6.45")
elif entreeinput == 11:
	print("Prisha's Favorite Chicken n' Cheese Enchiladas:" + "$7.84")
if breadandriceinput == 13:
	print("Cumin Rice: " + "               $2.25")
elif breadandriceinput == 14:
	print("Egg Fried Rice: " + "           $3.25")
elif breadandriceinput == 15:
	print("Plain Kulcha: " + "             $1.50")
elif breadandriceinput == 16:
	print("Aloo Kulcha: " + "              $2.25")
if dessertinput == 18:
	print("King-Sweets: " + "              $3.75")
elif dessertinput == 19:
	print("Coconut Fried Ice Cream: " + "  $2.50")
elif dessertinput == 20:
	print("Supreme Vanilla Fudge: " + "    $3.75")
if drinkinput == 22:
	print("Chai: " + "                     $1.00")
elif drinkinput == 23:
	print("Cookies n' Cream Milkshake:" + "$2.50")
elif drinkinput == 24:
	print("Bottle of Water: " + "         $1.25")
elif drinkinput == 25:
	print("Fountain Drink: " + "          $2.50")
totalcost = round(item_price_app + item_price_ent + item_price_brice + item_price_des + item_price_dri, 2) 
print("Order Name:" +                               menuname)
print("   Total:"     +         str              (totalcost))
taxresult = round(totalcost*0.0775, 2)
print("   Tax:"        +        str              (taxresult))
mysubtotal = round(totalcost+taxresult, 2)
print("   Subtotal:"    +      str              (mysubtotal))
print("-------HEAD TO THE CASHIER TO PAY-------")
print("  --Thank you For Choosing Fire n' Fusion--")
print("   *********ENJOY YOUR MEAL!*********"   )
