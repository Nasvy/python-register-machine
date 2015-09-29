"""
>>>In this Application We create a register machine 
>>>when you use a Gold card you gonna recieve a discount of 5%
or if you use a Silver card you gonna recieve a discount of 2%
>>>
"""
print """
"""
import os
import sys 
TOTAL= 0.0
PRIC = {}
INV = {}
def DISCOUNT():
	CARD = raw_input("Do you have a gold or silver card?\n")
	CARD = CARD.lower()
	if CARD == "gold" or CARD == "gold card":
		REDUCTION =	TOTAL * 0.5
		TOTAL = TOTAL - REDUCTION
		return TOTAL
	elif CARD == "silver" or CARD == "silver card":
		REDUCTION = TOTAL * 0.2
		TOTAL = TOTAL - REDUCTION
		return TOTAL	
#here the cashier can insert another articles
def QUESTION():
	QUEST = raw_input("Do you want to Insert another article? Y/N or you're Done?\n")
	QUEST = QUEST.lower()
	if QUEST == "y" or QUEST == "yes":
		ARTICLES()
	elif QUEST == "n" or QUEST == "no":
		MENU()
	elif QUEST == "Done":
		pass
	else:
		print "Insert a valid option"
		QUESTION()
#Here the Cashier insert the articles
def ARTICLES():
	ART = True
	ASD = False
	while ASD == False:
		ARTICLE = raw_input("...Insert first article\n")
		try:
			if  str(ARTICLE).isalpha() == True:
				print "Article Added"
				ASD = True
			else:
				print "Error"
				ASD = False
				raw_input("press enter to continue")
		except ValueError:
			print "Error Insert Article Again... "
		INV[ARTICLE]=""
		PRIC[ARTICLE]=""
	QUAN = True
	while QUAN == True:
		QUANTITY = raw_input("Insert Quantity article\n")
		INV[ARTICLE]= QUANTITY
		try:
			if int(QUANTITY):
				QUAN = False
			else:
				print "Only integer numbers"
				QUAN = True
		except ValueError:
			print "Only numbers"
		INV[ARTICLE]=QUANTITY
	PRI = True
	while PRI == True:
		PRICE = raw_input("Insert the price of the article\n")
		PRIC[ARTICLE]= PRICE
		try:
			if float(PRICE):
				QUESTION()
				PRI = False
			else:
				print "Only float numbers"
				PRI = True
		except ValueError:
			print "Only Float numbers"
			PRI = True
		PRIC[ARTICLE]=PRICE

#Here we create a function that allow to the user an option to get out
def EXIT():
	print "Thanks for Visit Us"
	raw_input("Press Enter for Continue ...")
	sys.exit()
#Here we create a menu that shows the options that user can select!
def MENU():
	while True: 
		os.system("cls")
		print "Welcome, please select an option\n"
		print "#1 Add an item "
		print "#2 Sell Articles"
		print "#3 Exit"
		DATA=raw_input("Insert an Option\n")
		if DATA =="1":
			ARTICLES() 
		elif DATA == "2":
			print PRIC
			print INV
			raw_input("Press enter")
		elif DATA == "3":
			EXIT()
		else:
			print "No entiendo la instruccion"
			raw_input("press enter to continue")
			os.system("cls")
           	os.system("clear")
MENU()