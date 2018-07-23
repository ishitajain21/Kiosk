
while True:
 
 import getpass
 
 p=getpass.getpass("Euphemism:")
 print("Computer,forcast this question and help me.")
 input("Question:")
 
 print(p)
 
 A=input("If you want directions, press D.If you want to break, press B. If you want to continue, press C.")
 
 if A=="D":
  print("In the first box, type the answer that you want to have. In the 2nd box the question that you want the answer to belong to.")
  continue
 
 if A=="B":
  break
 
 if A=="C":
  continue
 
 else:
  print("wrong value.")
  continuepeteranswers,
