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
SELL = {}
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
		INPUTS()
	elif QUEST == "n" or QUEST == "no":
		MENU()
	elif QUEST == "Done":
		pass
	else:
		print "Insert a valid option"
		QUESTION()
#Here the Cashier insert the articles
def ARTICLE():
	ART = True
	while True:
		ARTICLE = raw_input("Insert first article\n")
		try:
			if int(ARTICLE) == True:
				print "U"
			print "Error Insert Article Again... "
			raw_input("press enter to continue")
		except:
			print "Article Added"
			break
	QUANTITY()
def QUANTITY():
	QUAN = True
	while QUAN == True:
		QUANTITY = raw_input("Insert Quantity article\n")
		try:
			int(QUANTITY)
			PRICE()	
			return False
		except ValueError:
			print "Only numbers"
def PRICE():
	PRI = True
	while PRI == True:
		PRICE = float(raw_input("Insert the price of the article\n"))
		try:
			float(PRICE)
			QUESTION()
			PRI = False
		except ValueError:
			print "Only numbers"
def Sell():
	SELL [ARTICLE] = QUANTITY, PRICE
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
		DATA=input("Insert an Option\n")
		if DATA ==1:
			ARTICLE() 
		if DATA == 2:
			print SELL
		elif DATA == 3:
			EXIT()
		else:
			print "No entiendo la instruccion"
			raw_input("press enter to continue")
MENU()