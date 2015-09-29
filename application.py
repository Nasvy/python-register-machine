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
PRIC = {}
INV = {}
MULTY = 0
TOTAL = 0
#def INVOICE():
    #pass

def DONE():
    TOTAL = 0
    for i in PRIC:
        MULTY = float(PRIC[i]) * float(INV[i])
        print "The total of "+ i + " is: " + str(MULTY) +"$\n"
        TOTAL = MULTY + TOTAL
    #TOTAL = TOTAL
    print "Invoice Total is: " + str(TOTAL)
    raw_input("Press enter")
    os.system("cls")

    PREG = True
    while PREG== True: 
        try:
            HAVE = raw_input("Do you have a card? y/n\n")
            HAVE = HAVE.lower()
            if HAVE == "y" or HAVE == "yes":
                CARD = raw_input("Do you have a gold or silver card? \n")
                CARD = CARD.lower()
                try:
                    if CARD == "gold" or CARD == "gold card":
                        REDUCTION = TOTAL * 0.05
                        TOTAL = TOTAL - REDUCTION
                        print "Your total is :" + str(TOTAL)
                        raw_input("Press enter")
                        os.system("cls")
                        PREG = False
                    elif CARD == "silver" or CARD == "silver card":
                        REDUCTION = TOTAL * 0.02
                        TOTAL = TOTAL - REDUCTION
                        print "Your total is :" + str(TOTAL)
                        os.system("cls")
                        raw_input("Press enter")
                        PREG = False
                    else: 
                        print "This card doesn't exists"
                except ValueError:
                    print "insert a valid opction"
                    PREG = True
            elif HAVE == "n" or HAVE == "no":
                print "Your total is :" + str(TOTAL)
                os.system("cls")
                raw_input("Press enter")
        except ValueError:
            print "Insert a valid option"
            PREG = True

def BEST_SELLER():
    for i in PRIC:
        print "Article: "+i
        print "The cost is "+str(PRIC[i])
    for i in INV:
        if INV[i] > 1:
            print "In the Store are " +str(INV[i])+ " "+ i + "s\n"
        elif INV[i] <= 1:
            print "There are " +str(INV[i])+ " "+ i + " In the Store\n"
    OK = raw_input("...Are you done to continue to the invoice? y/n\n")
    OK = OK.lower()

    if OK == "y" or OK == "yes":
        DONE()
    elif OK == "n" or OK == "no":
        QUESTION()
#def DISCOUNT():
     
#here the cashier can insert another articles
def QUESTION():
    QUEST = raw_input("Do you want to Insert another article? Y/N or you're Done?\n")
    QUEST = QUEST.lower()
    if QUEST == "y" or QUEST == "yes":
        os.system("cls")
        ARTICLES()
    elif QUEST == "n" or QUEST == "no":
        MENU()
    elif QUEST == "done":
        BEST_SELLER()
    else:
        print "Insert a valid option"
        QUESTION()
#Here the Cashier insert the articles
def ARTICLES():
    ART = True
    ASD = False
    while ASD == False:
        ARTICLE = raw_input(">>>Insert an article<<<\n")
        try:
            if  str(ARTICLE).isalpha() == True:
                print "Article Added"
                INV[ARTICLE]=""
                PRIC[ARTICLE]=""
                ASD = True
            else:
                print "Error"
                ASD = False
                raw_input(">>>press enter to continue<<<")
        except ValueError:
            print "***Fatal Error*** \n Insert Article Again***"

    QUAN = True
    while QUAN == True:
        QUANTITY = raw_input(">>>Insert Quantity article<<<\n")
        try:
            if int(QUANTITY):
                INV[ARTICLE]= QUANTITY
                QUAN = False
            else:
                print "***Fatal Error*** \n Only integer numbers!"
                QUAN = True
        except ValueError:
            print "Only numbers!!"
    PRI = True
    while PRI == True:
        PRICE = raw_input(">>>Insert the price of the article<<<\n")
        try:
            if float(PRICE):
                PRIC[ARTICLE]= PRICE
                os.system("cls")
                PRI = False
                QUESTION()
            else:
                print "***Fatal Error*** \n Only float numbers"
                PRI = True
        except ValueError:
            print ">>>Only Float numbers<<<"
            #PRI = True

#Here we create a function that allow to the user an option to get out
def EXIT():
    print "Thanks for Visit Us n.n"
    raw_input(">>>Press Enter for Continue<<<")
    sys.exit()
#Here we create a menu that shows the options that user can select!
def MENU():
    while True: 
        os.system("cls")
        print "Welcome, please select an option\n"
        print "#1 Add an item "
        print "#2 Sell Articles"
        print "#3 Exit"
        DATA=raw_input(">>>Select an Option<<<\n")
        if DATA =="1":
            ARTICLES() 
        elif DATA == "2":
            BEST_SELLER()
        elif DATA == "3":
            EXIT()
        else:
            print "***Fatal Error***\n I don't understand the Instruction"
            raw_input("press enter to continue")
            os.system("cls")
            os.system("clear")
MENU()