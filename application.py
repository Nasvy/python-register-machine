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
BILL={}
#def INVOICE():
    #pass

def DONE():
    PREG = True
    while PREG == True:
        for i in INV:
            BUY = raw_input("Which article or articles do you want to buy?")
            BUY = BUY.lower()
            if BUY == BUY in INV and INV[i]>=0:
                ADD = LIST.append(BUY)
                print "In your shopping cart are: \n" + str(LIST)
                VAR = LIST.count(i)
                BILL[BUY]= VAR
                PREG = True
            elif BUY == "gold" or BUY == "gold card" or BUY == "silver" or BUY == "silver card":
                ADD = LIST.append(BUY)
                print "In your shopping cart are: \n" + str(LIST)
            elif BUY == "done":
                TOTAL = 0
                for i in PRIC:
                    if i == i in LIST:
                        MULTY = float(PRIC[i]) * float(BILL[i])
                        print "The total of "+ i + " is: " + str(MULTY) +"$\n"
                        TOTAL = MULTY + TOTAL
                for i in LIST:
                    if "gold" in LIST or "gold card" in LIST:
                        print "Invoice Subtotal is: " "%.2f" %float(TOTAL)
                        REDUCTION = TOTAL * 0.05
                        TOTAL = TOTAL - REDUCTION
                        print "Your Total with discount is: " "%.2f" %float(TOTAL)
                        TOTAL = (TOTAL * 0.12) + TOTAL
                        print "Your total is :" + "%.2f" % float(TOTAL)
                        raw_input("Press enter")
                        os.system("cls")
                        RESET()
                        MENU() 
                    elif "silver" in LIST or "silver card" in LIST:
                        REDUCTION = TOTAL * 0.02
                        TOTAL = TOTAL - REDUCTION
                        TOTAL = (TOTAL * 0.12) + TOTAL
                        print "Your total is: " "%.2f" %float(TOTAL)
                        raw_input("Press enter")
                        os.system("cls")
                        RESET()
                        MENU()
                    elif "silver" in LIST and "gold" in LIST:
                        print "Invoice Total is: " "%.2f" %float(TOTAL)
                        REDUCTION = TOTAL * 0.05
                        TOTAL = TOTAL - REDUCTION
                        TOTAL = (TOTAL * 0.12) + TOTAL
                        print "Your total is: " + "%.2f" % float(TOTAL)
                        raw_input("Press enter")
                        os.system("cls")
                        RESET()
                        MENU()
                    else:
                        print "Invoice Total is: " "%.2f" %float(TOTAL)
                        TOTAL = (TOTAL * 0.12) + TOTAL
                        print "Your total is: "  "%.2f" % float(TOTAL)
                        raw_input("Press enter")
                        os.system("cls")
                        RESET()
                        MENU()
        #raw_input ("Press enter")

def RESET():
    del LIST[0:]
def BEST_SELLER():
    for i in PRIC:
        print "Article: "+i
        print "The cost is "+str(PRIC[i])
    OK = raw_input("...Are you done to continue to the invoice? y/n\n")
    OK = OK.lower()

    if OK == "y" or OK == "yes":
        DONE()
        os.system("cls")
    elif OK == "n" or OK == "no":
        QUESTION()
#def DISCOUNT():
     
#here the cashier can insert another articles
def QUESTION():
    QUEST = raw_input("Do you want to Insert another article? Y/N\n")
    QUEST = QUEST.lower()
    if QUEST == "y" or QUEST == "yes":
        os.system("cls")
        ARTICLES()
    elif QUEST == "n" or QUEST == "no":
        MENU()
    else:
        print "Insert a valid option"
        QUESTION()
#Here the Cashier insert the articles
def ARTICLES():
    ART = True
    ASD = False
    while ASD == False:
        ARTICLE = raw_input(">>>Insert an article<<<\n")
        ARTICLE = ARTICLE.lower()
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