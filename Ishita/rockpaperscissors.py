import getpass
print("Let's play a rock paper scissors game. I guarentee, it will be fair.")

use1 = input("Alright, first person, what is your name?")
use2 = input("What is your name, other person?")

print("Great!")

while True:
    print("Let's play! Enter 1 for rock. 2 for paper. 3 for Scissors.")
    print("What is your move,",use1)
    use1move = getpass.getpass("?")
    print("Now what is your move,", use2)
    use2move = getpass.getpass("?")
    
    if use1move == "1" or "2" or "3":
        if use2move == "1" or "2" or "3":
    
            if use1move == use2move:
                print("It's a tie! Settle it next round.")
            else:
                if use1move == "1":
                    if use2move == "2":
                        print(use2,"Won!")
                    else:
                        print(use1,"Wins!")
                else:
                    if use1move == "2":
                        if use2move == "3":
                            print(use2,"Won!")
                        else:
                            print(use1,"Wins!!")
                    
                    else:
                        if use1move == "3":
                            if use2move == "1":
                                print(use2, "Won!")
                            else: 
                                print(use1, "Won!")
                        else:
                            print("Wierd answer given. Try again.")
