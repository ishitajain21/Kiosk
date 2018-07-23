while True:
    
    print("Hello. I am the numbergame. You can use me and we can play a game. Enter X for break.")
    
    import random
    a = int(random.randint(0,20))
    
    print("I have thought of a number and it is between 0 and 20. Try to guess it.\n\n")
    
    b=a*5
    c=b+(a*2)
    d=c+b+a
   
    print("I have some clues.Let us assign variables. A = my number. B = my number times 5. C = B+ (a times2 ). D= C+B+A\n\n")
    print("b=\n")
    print(b)
    print("\nc=\n")
    print(c)
    print("\nd=\n")
    print(d)
    
    e = int(input("\n\nI know it is very confusing. Go ahead and guess.\n\n"))
    
    if e == "X":
        break
    
    if e != a: 
        print("Sorry. Let's try another number.\n\n\n\n")
    
    if e == a:
        print("You got it! Maybe we can try another one.\n\n\n\n")
    
