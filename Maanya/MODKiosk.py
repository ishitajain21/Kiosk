def modkiosk():
    import sys
    menuname = 'To Be Determined later'
    questioninput = 0  
    pzzaq = 0
    sizepizza = 0
    def myintro():
        global questioninput
        global menuname
        print("Hello I am MODBot, welcome to MOD Pizza. Please choose your item in each category.")
        print("When I ask for your choices enter the code of the menu item.")
        menuname= str(input("What is the name you would like your order placed under:"))
        questioninput = int(input("Would like to eat here or would you like your order to-go? Enter 1 for eating here and 2 if you would like your meal to-go:"))
        if questioninput < 1 or questioninput > 2:
            sys.exit("Sorry there was an error in your input. Please retry!")
            print(modkiosk())
        return
    def pizzas():
        global pizzaq
        global sizepizza
        pizzaq = int(input("Enter 1-If you want to Create Your Own Pizza... Enter 2-If you would like to Order a Specialty Pizza...Enter 3-If you would like to order something else:"))
        if pizzaq == '1':
            print("Choose a Pizza Size")
            print("------------------------")
            print("Enter 1 --- Mini(6-inch pizza) ~ $6.47")
            print("Enter 2 --- MOD(11-inch pizza) ~ $8.47")
            print("Enter 3 --- Mega Dough(11-inch thick crust pizza) ~ $10.47")
            sizepizza = int(input("Enter 1, 2, or 3:"))
            if sizepizza > 3 or sizepizza < 1:
                sys.exit("Sorry there is an error in your input! Try again!")
                print(modkiosk)
            elif sizepizza =='1' or sizepizza == '2' or sizepizza == '3':
                print("Choose a Sauce")
                print("------------------------")
                print("Enter 1 --- BBQ Sauce")
                print("Enter 2 --- Garlic Rub")
                print("Enter 3 --- Olive Oil")
                print("Enter 4 --- Pesto")
                print("Enter 5 --- Red Sauce")
                print("Enter 6 --- White Sauce")
                print("Enter 7 --- No Sauce")):
