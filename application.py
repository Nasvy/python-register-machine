"""
In this Application We create a register machine 
"""
print """
"""
import os
import sys 
TOTAL= 0.0
def EXIT():#Here we created an function that allow to the user an option to get out
	print "Thanks for Visit Us"
	raw_input("Press Enter for Continue n.n")
	sys.exit()

def Menu():#Here we menu that shows the options that user can select!
	while True: 
		os.system("cls")
		print "Welcome, please select an option\n"
		print "#1 Add an item "
		print "#2 Sell Articles"
		print "#3 Exit"
		DATA=raw_input("Insert an Option\n")
		"""if DATA =="1":
			TOTAL =  
		elif DATA == "2":
		"""	
		if DATA == "3":
			EXIT()
		else:
			print "No entiendo la instruccion"
			raw_input("press enter to continue")
Menu()