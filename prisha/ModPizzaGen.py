lobal namelist
namelist={"Test":'Testflavor'}

def NamePick():
    global name
    global OldNew
    name=input("what is your name???")
    #for item in namelist :
    if name in namelist:
        #print (namelist, name)
        OldNew = input("welcome back would you like a new flavor your previous flavor 1=new 2=old")
    else :
        OldNew  = '1'

        
    
def FlavorPick():
    a="Maddy" 
    b="Mad Dog" 
    c="Tristan"
    d="Dominic"
    e="Lucy Sunshine"
    f="Jasper" 
    g="Dhillion James"
    h="Calexico"
    i="Caspain"
    j="Pizza Salad"
    k= "Isaac"

    #Shiv : Consider being very precise.
    #Shiv : Telling about the program should happen first.
    #Shiv : Telling about the program is not the job of this function.
    #Shiv : This function is just about picking your flavor.
    
    print ("this program will finally solve your Mod Pizza classic pizza problems by printing a flavor randomly")
    import random 
    global choice
    choice= random.choice('abcdefghijk')


    if 'a'==choice:
        print("Maddy: Classic Cheese Pizza")
    if 'b'==choice:
        print("Mad Dog: mozzarella, pepperoni, mild sausage, ground beef, red sauce")
    if 'c'==choice:
        print ("Tristan:mozzarella, asiago, roasted red peppers, mushrooms, pesto")
    if 'd'==choice:
        print ("Dominic:white sauce, asiago, fresh chopped basil, red onion, sliced tomatoes, mild sausage")
    if 'e'==choice:
        print ("Lucy Sunshine: mozzarella, parmesan, artichokes, garlic, dollops of red sauce")
    if 'f'==choice:
        print ("Jasper: mozzarella, mushrooms, spicy italian sausage, red sauce")
    if 'g'==choice:
        print("Dillion James:mozzarella, asiago, fresh chopped basil, garlic, sliced tomatoes, red sauce")
    if 'h'==choice:
        print("Calexico:mozzarella, gorgonzola, chicken, jalapenos, hot buffalo sauce, red sauce")
    if 'i'==choice:
        print ("Caspain: mozzarella, gorgonzola, bbq chicken, barbecue sauce, sliced red onions")
    if 'j' == choice :
        print ("Pizza Salad:Create your own salad on a warm asiago pizza crust")
    if 'k' == choice:
        print ('Isaac: Olive Oil, Garlic, Ricotta , Red Onion,Roasted Grape Tomatoes, Balsamic Vinaigrette, and Basil')
        
    Savingname(name,choice)
        
def OldFlavorPick (MyChoice):
    a="honey lavendar" 
    b="original strawberry" 
    c="sweet cream"
    d="earl grey"
    e="maple walnut"
    f="scout mint" 
    g="stumptown coffe"
    h="salte1d caremal"
    i="melted chocolate"
    j="cookie dough"
    
    if 'a'==choice:
        print("your choice is honey lavendar")
    if 'b'==choice:
        print("your choice is original strawberry")
    if 'c'==choice:
        print ("your choice is sweet cream")
    if 'd'==choice:
        print ("your choice is earl grey")
    if 'e'==choice:
        print ("your choice is maple walnut")
    if 'f'==choice:
        print ("your choice is scout mint")
    if 'g'==choice:
        print("your choice is salted caremal")
    if 'i'==choice:
        print("your choice is melted chocolate")
    if 'j'==choice:
        print ("your choice is cookie dough")
    
def Savingname(name,choice):
    #takes name and choice and writes that to a dictionary
    #global namelist
    namelist[name]= choice
    print ("Saving you in our records",namelist)
    

        

var=1
while var==1:
    print ("----------------Start Processing--------------------")
    NamePick()
    print(OldNew)
    if OldNew == '2':
        myChoice= (namelist[name])
        OldFlavorPick(myChoice)
    if OldNew == '1':
        FlavorPick()
    
