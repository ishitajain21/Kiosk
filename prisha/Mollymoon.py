global namelist

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



    #Shiv : Consider being very precise.

    #Shiv : Telling about the program should happen first.

    #Shiv : Telling about the program is not the job of this function.

    #Shiv : This function is just about picking your flavor.

    

    print ("this program will finally solve your ice cream choosing problems by printing a flavor randomly")

    import random 

    global choice

    choice= random.choice('abcdefghij')





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
