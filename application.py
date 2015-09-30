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
LIST=[]
#def INVOICE():
    #pass

def DONE():


    PREG = True
    while PREG == True:
        for i in INV:
            print INV
            ART = 0
            BUY = raw_input("Which article or articles do you want to buy?")
            if BUY == BUY in INV and INV[i]>=0:
                INV[BUY] = int(INV[BUY])-1
                ADD= LIST.append(BUY)
                print LIST
                PREG = True
                VAR = LIST.count(i)
                print VAR
                raw_input("Press enter")
                EX = raw_input("Do you finish y/n \n")
                EX= EX.lower()
                if EX== "y" or EX == "yes":
                    PREGU = True
                    while PREGU== True: 
                        try:
                            HAVE = raw_input("Do you have a card? y/n\n")
                            HAVE = HAVE.lower()
                            if HAVE == "y" or HAVE == "yes":
                                CARD = raw_input("Do you have a gold or silver card? \n")
                                CARD = CARD.lower()
                                try:
                                    if CARD == "gold" or CARD == "gold card":
                                        TOTAL = 0
                                        for i in PRIC:
                                            if i == i in LIST:
                                                MULTY = float(PRIC[i]) * float(VAR)
                                                print "The total of "+ i + " is: " + str(MULTY) +"$\n"
                                                TOTAL = MULTY + TOTAL
                                        print "Invoice Total is: " + str(TOTAL)
                                        raw_input("Press enter")
                                        os.system("cls")
                                        REDUCTION = TOTAL * 0.05
                                        TOTAL = TOTAL - REDUCTION
                                        TOTAL = (TOTAL * 0.12) + TOTAL
                                        print "Your total is :" + str(TOTAL)
                                        raw_input("Press enter")
                                        os.system("cls")
                                        MENU()
                                        PREGU = False
                                        PREG = False
                                        break
                                    elif CARD == "silver" or CARD == "silver card":
                                        REDUCTION = TOTAL * 0.02
                                        TOTAL = TOTAL - REDUCTION
                                        TOTAL = (TOTAL * 0.12) + TOTAL
                                        print "Your total is :" + str(TOTAL)
                                        raw_input("Press enter")
                                        os.system("cls")
                                        MENU()
                                        PREGU = False
                                        PREG = False
                                        break
                                    else: 
                                        print "This card doesn't exists"
                                except ValueError:
                                    print "insert a valid opction"
                                    PREGU = True
                            elif HAVE == "n" or HAVE == "no":
                                TOTAL = (TOTAL * 0.12) + TOTAL
                                print "Your total is :" + str(TOTAL)
                                raw_input("Press enter")
                                os.system("cls")
                                return MENU()
                        except ValueError:
                            print "Insert a valid option"
                            PREGU = True
                elif EX == "no" or EX == "n":
                    PREG= True

            #elif BUY not in INV or INV[i] <=0:
                #print "Not more" + BUY + "In store"
                #PREG = True
                
    

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
    print "Thanks for Visit Us."
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