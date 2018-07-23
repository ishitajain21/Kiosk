

import random 

print("Hi! we are going toplay rock paper scissors.")

name = input("What is your name? ")

if True:
    move1 = int(input(" What is your move? Write 1 for rock. Write 2 for paper. Write 3 for scisors. "))
    a = int(random.randint(1,3))

    if a == 1:
        if move1 == 2:
            print(a,"Was my move.You won!")
        else:
            print(a," Was my move. I won!")
        
    else:
        if a == 2:
            if move1 == 3:
                print(a," Was my move. You won!")
            else:
                print(a,"Was my move. I won!")
    
        else:
            if a == 3:
                if move1 == 1:
                    print(a,"Was my move. You won!")
                else:
                    print(a,"Was my move.I won!")
            else:
                print("Wierd answer given.")


