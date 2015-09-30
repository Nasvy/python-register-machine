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
LIST = []
BILL = {}
def finish():
    """Here is the final part of the program"""
    print "When you're ready write 'Done'"
    preg = True
    while preg == True:
        for i in INV:
            buy = raw_input("Which article or articles do you want to buy?\n")
            buy = buy.lower()
            if buy == buy in INV and INV[i] >= 0:
                LIST.append(buy)
                print "In your shopping cart are: \n" + str(LIST)
                var = LIST.count(i)
                BILL[buy] = var
                preg = True
            elif buy not in INV and (buy != "silver") and (buy != "gold") and (buy != "done"):
                print "We don't have this item, insert a valid Item"
                raw_input("Press Enter")
                preg = True
            elif buy == "gold" or buy == "gold card" or buy == "silver" or buy == "silver card":
                LIST.append(buy)
                print "In your shopping cart are: \n" + str(LIST)
            elif buy == "done":
                finaly()
def finaly():
    """here make the bill for the user"""
    os.system("cls")
    total = 0
    for i in PRIC:
        if i == i in BILL:
            multy = float(PRIC[i]) * float(BILL[i])
            print "The price of total of your "+ i + "(s) is: " + str(multy) +"$\n"
            total = multy + total
    for i in LIST:
        if "gold" in LIST or "gold card" in LIST:
            print "Invoice Subtotal is: ........" "%.2f" %float(total)
            total = (total * 0.12) + total
            print "Your total with IVA is: ....." "%.2f" % float(total)
            reduction = total - (total * 0.05)
            print "Your total with discount is: " "%.2f" %float(reduction)
            print "_____________________________________"
            raw_input("Press enter")
            os.system("cls")
            reset()
            menu()
        elif "silver" in LIST or "silver card" in LIST:
            print "Invoice Subtotal is: ........" "%.2f" %float(total)
            total = (total * 0.12) + total
            print "Your total with IVA is: ....." "%.2f" %float(total)
            reduction = total - (total * 0.02)
            print "Your total with discount is: " "%.2f" %float(reduction)
            print "_____________________________________"
            raw_input("Press enter")
            os.system("cls")
            reset()
            menu()
        elif "silver" in LIST and "gold" in LIST:
            print "Invoice Subtotal is: ........" "%.2f" %float(total)
            reduction = total - (total * 0.05)
            total = (total * 0.12) + total
            print "Your total with IVA is: ....." "%.2f" % float(total)
            print "_____________________________________"
            total = total - reduction
            print "Your total with discount is: " "%.2f" %float(reduction)
            raw_input("Press enter")
            os.system("cls")
            reset()
            menu()
        else:
            print "Invoice total is: ..........." "%.2f" %float(total)
            total = (total * 0.12) + total
            print "Your total with IVA is ......" "%.2f" % float(total)
            raw_input("Press enter")
            os.system("cls")
            reset()
            menu()
def reset():
    """This function reset the list of articles"""
    del LIST[0:]
def best_seller():
    """This Function ask the user what does he wants to buy"""
    for i in PRIC:
        print "article: "+i
        print "The cost is "+str(PRIC[i])
    invoice = True
    try:
        while invoice == True:
            yes = raw_input("...Are you Done to continue to the invoice? y/n\n")
            yes = yes.lower()
            if yes == "y" or yes == "yes":
                finish()
                os.system("cls")
            elif yes == "n" or yes == "no":
                question()
            else:
                print "i dont understand"
                invoice = True
    except ValueError:
        print "Insert a valid option"
#here the cashier can insert another articles
def question():
    """This function ask the user if he wants to continue adding articles"""
    quest = raw_input("Do you want to Insert another article? Y/N\n")
    quest = quest.lower()
    if quest == "y" or quest == "yes":
        os.system("cls")
        articles()
    elif quest == "n" or quest == "no":
        menu()
    else:
        print "Insert a valid option"
        question()
#Here the Cashier insert the articles
def articles():
    """Here the User insert the articles and the prices"""
    asd = False
    while asd == False:
        article = raw_input(">>>Insert an article<<<\n")
        article = article.lower()
        try:
            if article == "done":
                print "You can't write done here!"
                question()
                os.system()
            if  str(article).isalpha() == True:
                print "article Added"
                INV[article] = ""
                PRIC[article] = ""
                asd = True
            else:
                print "Error"
                asd = False
                raw_input(">>>press enter to continue<<<")
        except ValueError:
            print "***Fatal Error*** \n Insert article Again***"

    pri = True
    while pri == True:
        price = raw_input(">>>Insert the price of the article<<<\n")
        try:
            if float(price):
                PRIC[article] = price
                os.system("cls")
                pri = False
                question()
            else:
                print "***Fatal Error*** \n Only float numbers"
                pri = True
        except ValueError:
            print ">>>Only Float numbers<<<"
#Here we create a function that allow to the user an option to get out
def out():
    """This function exits the program"""
    print "Thanks for Visit Us."
    raw_input(">>>Press Enter for Continue<<<")
    sys.exit()
def menu():
    """Here we create a menu that shows the options that user can select!"""
    while True:
        os.system("cls")
        print "Welcome, please select an option\n"
        print "#1 Add an item "
        print "#2 Sell articles"
        print "#3 exit"
        data = raw_input(">>>Select an Option<<<\n")
        if data == "1":
            articles()
        elif data == "2":
            best_seller()
        elif data == "3":
            out()
        else:
            print "***Fatal Error***\n I don't understand the Instruction"
            raw_input("press enter to continue")
            os.system("cls")
            os.system("clear")
menu()
