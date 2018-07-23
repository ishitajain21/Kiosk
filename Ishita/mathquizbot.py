import random
global w

print("Welcome, to Math QuizBot ! ")
print("Just so we can help you understand concepts better,")
b = input("What is your friend's name?(You can make up one if it makes you feel comfortable)")
    
def awake():
    a = input("Ready to go on?")
    
def howtoadd(number):
    print("\n--------------------How to add----------------------------------------")
    if "1" == number:
        print("\nAddition is basically the adding of two quantities together. Like if you have 5 apples and", b , " gave you 2 more, you now have 7 apples.! You can easily draw that by making the number the sticks.")
        print("\nGet comfortable with the concept of adding. Take a handful of beans (or other small objects). Set one bean aside at a time into a pile and count each one as you go (1, 2, 3, etc).")
        print("\nStop after you have a few beans in the pile. How many did you put there? Write that number down. ")
        awake()
        print("\n\n\n\nNow, do the same thing but make another pile. Now, put the two piles together. How many do you have now? You can count up each bean, one at a time, and find out! This is adding!")
        print("\nFor example, your first pile might have 5 beans. Then your second pile might have 3 beans. When you put the two piles together and count all the beans, you'll find that you now have 8 beans! This is because 5 + 3 is 8.")
        print("\nLearn the number pairs. Since most people base counting on sets of ten and numbers divisible by ten you can make adding much easier by learning what number pairs add up to ten. Examples include: 1+9, 2+8, 3+7, 4+6, and 5+5.")
        print("\nDouble check using your hands! When you can, you can always double check your math using your fingers or another method, such as making marks to keep extra ones and for groups of 5 and 10. Players often add tally marks for keeping the score/'the tally' in a game such as dominoes.")
        awake()
        
    if "2" == number:
        print("\nAddition is basically the adding of two quantities together. Like if you have 5 apples and", b , " gave you 2 more, you now have 7 apples.! You can easily draw that by making the number the sticks.")
        awake()
        
def howtosubtract(number):
    print("\n----------------How to subtract---------------")
    if "1" == number:
        print("\nSubtraction is the opposite of addition.When ", b, "gave you 2 apples and you had 5 apples, you have 7. Let's say", b, "comes back and asks you for 1 apple. You had 7 but you gave her 1 , you have 6. You can also do that by sticks.")
        print("\n\nRule 1: Subtracting a positive number from a positive number—this is normal subtraction.Example 1: Don’t let all this talk of positive and negative numbers throw you off track—if you see a positive number minus a positive number, subtract it like normal! For example, if you see 5 – 3, subtract normally! 5 – 3 = 2.")
        print("\n\n\n Rule 2: Subtracting a positive number from a negative number—start at the negative number, and count backwards the additional amount you’re subtracting.Example 2: Let’s say we had the problem -5 – 3. This would be read as “negative five minus three.” This can be thought of on a number line, which means we’re going to start at the negative number (-5) and keep counting back the -3, arriving at -8, like this:")
        print("\n\n\nThus, -5 – 3 = -8.You can also think about these problems as addition problems—you add the numbers together (5 + 3 = 8) and then, since both numbers have a minus sign in front of them, you would add a negative sign in front of your answer, like this: -8. If this makes more sense, you can do these problems like this—but only problems that are written like this: -5 – 3. If there are any other signs (addition, subtraction, etc) you need to follow the rule for that type of problem.")
        print("\n\nRule 3: Subtracting a negative number from a negative number—when you see the subtraction (minus) sign followed by a negative sign, turn the two signs into a plus sign. Thus, instead of subtracting a negative, you are adding a positive. So, – -5 becomes +5, and continue normally with the addition.Example 3: Let’s say we had the problem -6 – -3. This would be read as “negative six minus negative three.” This can be thought of on a number line, which means we’re going to start at by changing the – -3 into +3,")
        print("\n\nRule 4: Subtracting a negative number from a positive number—when you see the subtraction (minus) sign followed by a negative sign, turn the two signs into a plus sign. Thus, instead of subtracting a negative, you’re adding a positive, so you have a simple addition problem.Example 4: Let’s say we had the problem 5 – (-3). This would be read as “five minus negative three.” This would work the same way as the previous example, so the – (-3) would change to a +3; therefore, your new problem would read 5 + 3, which is a simple addition problem, resulting in 8.")
        print("\nFor subtraction, when doing like 3 - 4, switch the order = 4-3. The answer is 1 right? No. We must add a negative to the 1 to show that the number is smaller.")
    
    if "2" == number:
        print("\nSubtraction is the opposite of addition.When ", b, "gave you 2 apples and you had 5 apples, you have 7. Let's say", b, "comes back and asks you for 1 apple. You had 7 but you gave her 1 , you have 6. You can also do that by sticks.")
    
    
def howtomultiply(number):
    print("\n--------------How to multiply-----------------------")
    if "1" == number:
        print("\nMultiplication is repeated addition. 7 * 2 = 7 plus 7 (You are doing 7 + 2 times). You can also do this by sticks. A bundle of 7 sticks. And we have 2 bundles. SO the total sticks we have is 14.")
        print("\nWrite down the problem. You are solving the problem 4 x 3. This is really another way to say '3 groups of four.'You can think of this as repeated addition, where the number four will be repeated 3 times. But you are adding the number the amount of times you want to multiply it by.")
        print("\nSolve through repeated addition. Knowing that each of the four groups have three objects, add 4 three times. 4 + 4 + 4 = 12. You can also find 4 groups of 3 instead. This will give you the same answer. Just add up the numbers in the problem 3 + 3 + 3 + 3 and you will get 12, the same answer.")
    if "2" == number:
        print("\n Multiplication is repeated addition. 7 * 2 = 7 plus 7 (You are doing 7 + 2 times). You can also do this by sticks. A bundle of 7 sticks. And we have 2 bundles. SO the total sticks we have is 14.")

# This is for people who need help.
def help(num):
    howtoadd(num)
    howtosubtract(num)
    howtomultiply(num)
    
    print("You can always scroll up for reference of this. ")
    awake()
    levelone()

# This basically is the number of wrongs there is.
w = 0 

# This function does the checking process. 
def check_results_and_get_them(actualanswer):
    answerinput= int(input(""))
    if answerinput == actualanswer:
        print("Yup!")
        awake()
    else:
        print("Nope")
        print("The correct answer is :")
        print(actualanswer)
        awake()
        global w
        w = w +1
        
def addition(starting, ending):
    rand= int(random.randint(starting, ending))
    rand_two = int(random.randint(starting,ending))
    actualanswer = rand + rand_two
    print("\n", rand, "+", rand_two,"=" )
    check_results_and_get_them(actualanswer)
    
def multiplication(starting,ending):
    rand= int(random.randint(starting, ending))
    rand_two = int(random.randint(starting,ending))
    actualanswer = rand * rand_two
    print("\n", rand, "*", rand_two,"=" )
    check_results_and_get_them(actualanswer) 
    
def subtraction(starting,ending):
    rand= int(random.randint(starting, ending))
    rand_two = int(random.randint(starting,ending))
    if rand < rand_two:
        print("Trick question:")
    actualanswer = rand - rand_two
    print("\n", rand, "-", rand_two,"=" )
    check_results_and_get_them(actualanswer) 
    
def rand(starting, ending):
    rand= int(random.randint(starting, ending))
    rand_two = int(random.randint)
    
def goontonextlevel(number,levelpass,levelfail,):
    if w <= number:
        print("No, I am sorry but you must repeat this level.")
        levelfail    
    if w > number:
        
        w = 0 
        print("Yes, we are moving on.")
        levelpass

def levels( n1, n2,forisa, forism, foriss):
    print("-----------------------Addition------------------------")
    for i in range(0,forisa):
        addition(n1, n2)
    print("-----------------------Multilpication----------------- ")
    for i in range(0,forism):
        multiplication(n1, n2)
    print("---------------------Subtraction------------------------")
    for i in range(0,foriss):
        subtraction(n1, n2)
        
        
def levelsimply(level):
    howtoadd("2")
    howtomultiply("2")
    howtosubtract("2")
    
    if level < 7:
        print("---------------------------Level", level, "-------------------------------------------------")
    if level == 2:
        print("Hi! This level is basic. It teaches you your facts till 100.")
        levels(10,100,100,50,100)
        goontonextlevel(levelsimply(345),levelsimply(2),5)
    
    # There is a special level called 345
    if level == 345:
        print("To a 1000!")
        levels(100,1000,100,10,100)
        print("All right! Arsonist of Arithemetic! You are officialy in level 4 .")
        print("--------------------------------------Level 4 -------------------------------------------------")
        print("I know its hard- but that's why we re doing it. Sharpen your pencils! ")
        levels(100,1000,100,10,100)
        print("Astonishing! Magician of Multipliction, supervisor in subtraction and amazing at addition! Level 5!")
        print("-----------------------------------------Level 5 --------------------------------------------------------")
        print("10000! It was important because it will help you build up. ")
        levels(1000,10000,100,10,100)        
        goontonextlevel(levelsimply(6),15,levelsimply(345))
        
    if level == 6:
        print("Yup you are smart enough for rocket science! King of Math! Level 6!")
        print("Alright - Let's do this! From now on, you will just get another 0 every time.")
        print("Also if you get too many wrong in buildup, you must do it again. ")
        levels(10000,100000,100,10,100)     
        goontonextlevel(levelsimply(7),5,levelsimply(6))
        
    if level == 7:
        print("===================Level 7 ======================================================================")
        print("OMG!!!! The second badge - think of this like graduation...")
        levels(100000,1000000,50, 5, 50)
        goontonextlevel(levelsimply(7), levelsimply(8), 10)        
        
    if level == 8:
        print("===================================Level 8 =================================================")
        print("Nice job! You are now an emporer instead of king! Level 8!")
        print("This is going to get harder... Stretch and sit straight! Let's go.")
        levels(1000000,10000000,50,5,50)
        goontonextlevel(levelsimply(8), levelsimply(9), 12)
        
    if level == 9:
        print("=================================Level 9 =======================================================")
        print("Almost to the end!!!!")
        levels(10000000,100000000,50,5,50)
        goontonextlevel(levelsimply(9), levelsimply(10), 13)
    
    if level == 10:
        print("===================================Level 10 ===================================================")
        print("OMG! You are in the last and final level. It will test you like no other. Into Billions. Level 10!!")
        print("Take a breath! It will challenge you. ")
        levels(100000000,1000000000,50,5,50)
        if w >=15:
            print("I'm sorry, we must do this level again.")
            print("Because you had ", w , "wrong.")
            levelsimply(10)
        if w < 15:
            print("You have now reached! The medal of honor. Good job! Best!")
            test()
            exit

def levelone():
    print("______________________________________Level 1 ________________________________________________________")
    #basic level 1
    print("Well, hi! This level is basic - it teaches you your facts till 10.")
    print("----------------Addition--------------------")
    # Addition(Tests on it)
    for i in range(0,10):
        addition(0,10)
            
    print("On to - Multiplication!")
    
    print("--------------------Multiplication-----------------------")
    print("Remeber- Repeated addition- Go ahead and actually do it like that.")
    for i in range(0,1):
        
        multiplication(0,10)
        
    print("Whew! Just a bit more - to subtraction.")
    
    print("--------------------Subtraction---------------")
    print("Subtraction is the opposite of addition.")
    print("5+3 = 8 and 8- 3 +5 and 8 - 5 =3 ")
    for i in range (0,1):
         
        subtraction(0,10)
    
    goontonextlevel(levelsimply(2), levelone(), 5)
        
def test():
    print("So this is a test. It will test to see if you know all your basic levels.It stops at 100,000. But you should be really good at those!")
    print("::::::::::::::::::::::::::::::::::::::Test::::::::::::::::::::::::::::::::::::::::::::::::")
    for i in range(1000):
        addition(0,10)
    for i in range(1000):
        multiplication(0,10)
    for i in range(1000):
        subtraction(0,10)
        
    for i in range(100):
        addition(0,100)
    for i in range(100):
        subtraction(0,100)    
    for i in range(10000):
        subtraction(0,100)  
        
    for i in range(10):
        addition(0,1000)
    for i in range(10):
        subtraction(0,1000)    
    for i in range(10):
        multiplication(0,1000)    
        
    for i in range(10):
        addition(0,10000)
    for i in range(10):
        subtraction(0,10000)    
    for i in range(10):
        multiplication(0,10000)
        
    for i in range(10):
        addition(0,100000)
    for i in range(10):
       subtraction(0,100000)    
    for i in range(10):
        multiplication(0,100000)  
        
    if w > 50:
        print("Nope! Gonna have to repeat the test.")
        test()
        
    if w < 50:
        print("Yyyyyyyyyyyyyyeeeeeeeeeeeeeeeeeeesssssssssssssssss! You finished the whole quiz bot!!! Fist pummp !! Now you can exit and do your favorite levels or just exit. But please, come back!!")



print("Hello, I am math. You can practice math (arithmetic) with me.")
print("If you want to try this out, you must know how to work with negtive numbers and know how to add and subtract and multiply, fairly well.")

experience=input("Have you been here before? Enter no or yes.")

if ("no" == experience):
    print("Well, hello there!")
    print("\nThis is a program that helps you to polish your arithmetic(not division).")
    a = input(" Need help? Write' help  ")
    
    if a == "help":
        print("That's okay! ")
        
        help("1")
    levelone()
    
if("yes" == experience):
    print("Remember: 1 is one, 2 is two, 3 is three 6 is six, 7 is seven, 8 is eight, 9 is nine, 10 is ten or if you would like to do the test, write'test'.")
    print("If you did level 4 or 5, we will just start at level three(so write level three)")
    print("If you need help, write 'help' ")
    level = input ("Which level have you stopped at? only letters...   ")
    if level == "one":
        levelone()
    if level == "two":
        levelsimply(2)
    if level == "three":
        levelsimply(345)
    if level == "six":
        levelsimply(6)
    if level == "seven":
        levelsimply(7)
    if level == "eight":
        levelsimply(8)
    if level == "nine":
        levelsimply(9)
    if level == "ten":
        levelsimply(10)
    if level == "help":
        print(" So you need help, that's okay! ")
        help("1")
    if level == "test":
        test()
