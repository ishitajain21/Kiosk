def intro ():
	print("Hi, I am Yobot.")


def language():
	lang = int(input("Hi! Tell me if you speak: 1- English or 2- Bengali or 3- Hindi\n"))
	
	if lang == "1":
		print("Hello")
	else:
		if lang == "2":
			print("Nomoskar")
		else:
			if lang == "3":
				print("Namaste")
			else:
				print("Sorry, you entered an invalid value.")


def zodiac():
	x=int(input("Now enter your birth year from 1996 - 2012.\n"))
	print (x)
	for i in range(1):
	                print("Your zodiac is:")
	if x == "1996" or x=="2008":
		print(" a rat. Rat are intelligent, charming, quick-witted, practical, ambitious, and good at economizing as well as social activities. The weaknesses are that the Rats are likely to be timid, stubborn, wordy, greedy, devious, too eager for power and love to gossip.")
	else:
		if x=="1997" or x== "2009":
				print(" an ox.Ox are usually hard working, honest, creative, ambitious, cautious, patient and handle things steadily. On the negative side, Ox people might be stubborn, narrow-minded, indifferent, prejudiced, slow and not good at communication.")
		else:
				if x=="1998" or x=="2010":
						print(" a tiger.Tigers are the symbol of brave. People born in the year of the Tiger are friendly, brave, competitive, charming and endowed with good luck and authority. With indomitable fortitude and great confidence, the tiger people can be competent leaders. On the other side, they are likely to be impetuous, irritable, overindulged and love to boast to others.")
				else:
						if x=="1999" or x=="2011":
								print(" a rabbit. Rabbit are kind-hearted, friendly, intelligent, cautious, skillful, gentle, quick and live long. They dislike fighting and like to find solutions through compromise and negotiation. On the negative side, Rabbit people have the potential to be superficial, stubborn, melancholy and overly-discreet.")
						else:
								if x=="2000" or x=="2012":
										print(" a dragon.Dragon are powerful, kind-hearted, successful, innovative, brave, healthy courageous and enterprising. However, they tend to be conceited, scrutinizing, tactless, quick-tempered and over-confident.")
								else:
										if x=="2001" or x=="2002":
												print(" a snake.Snake are wise, discreet, agile, attractive and full of sympathy. On the other hand, there is a tendency for them to be lazy, greedy, arrogant and indulging in self-admiration.")
										else:
												if x=="2003":
														print(" a sheep.Sheep (also Goat or Ram) represents solidarity, harmony and calmness. People born in the year of the Sheep are polite, mild mannered, shy, imaginative, determined and have good taste. On the negative side, they are sometimes pessimistic, unrealistic, short-sighted and slow in behavior.")
												else:
														if x=="2004":
															print(" a monkey.Monkey are wise, intelligent, confident, charismatic, loyal, inventive and have leadership. The weaknesses of the Monkeys are being egotistical, arrogant, crafty, restless and snobbish.")
														else:
															if x=="2005":
																print(" a rooster.Rooster are beautiful, kind-hearted, hard-working, courageous, independent, humorous and honest. They like to keep home neat and organized. On the other side, they might be arrogant, self-aggrandizing, persuasive to others and wild as well as admire things or persons blindly.")
															else:
																if x=="2006":
																	print(" a dog. Dogs are honest, friendly, faithful, loyal, smart, straightforward, venerable and have a strong sense of responsibility. On the negative side, they are likely to be self-righteous, cold, terribly stubborn, slippery, critical of others and not good at social activities.")
																else:
																	if x=="2007":
																		print(" a pig.Pig are happy, easygoing, honest, trusting, educated, sincere and brave. The possible dark sides the Pig people are stubbornness, naive, over-reliant, self-indulgent, easy to anger and materialistic. They are sometimes regarded as being lazy.")
																	else:
																		print("NA. Sorry, your age is not in the program.")


intro()
language()			
zodiac()

