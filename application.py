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
SELL = {
	"PRICE" : []
}
def QUESTION():
	QUEST = raw_input("Do you want to Insert another article? Y/N\n")
	QUEST = QUEST.lower()
	if QUEST == "y" or QUEST == "yes":
		INPUTS()
	elif QUEST == "n" or QUEST == "no":
		MENU()
	else:
		print "Insert a valid option"
		QUESTION()
def INPUTS():
	ARTICLE= raw_input("Insert first article\n")
	QUANTITY = raw_input("Insert Quantity article\n")
	PRICE = float(raw_input("Insert the price of the article\n"))
	QUESTION()
def EXIT():#Here we create a function that allow to the user an option to get out
	print "Thanks for Visit Us"
	raw_input("Press Enter for Continue n.n")
	sys.exit()

def MENU():#Here we create a menu that shows the options that user can select!
	while True: 
		os.system("cls")
		print "Welcome, please select an option\n"
		print "#1 Add an item "
		print "#2 Sell Articles"
		print "#3 Exit"
		DATA=raw_input("Insert an Option\n")
		if DATA =="1":
			INPUTS()  
		#elif DATA == "2":
		if DATA == "3":
			EXIT()
		else:
			print "No entiendo la instruccion"
			raw_input("press enter to continue")
MENU()