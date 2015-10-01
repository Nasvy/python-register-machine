"""
>>>In this Application We create a register machine
>>>when you use a Gold card you gonna recieve a discount of 5%
or if you use a Silver card you gonna recieve a discount of 2%
>>>
"""
import os
import sys
PRIC = {}
INV = {}
LIST = []
BILL = {}
COMPRAS = []
def finish():
    """Here is the final part of the program"""
    print "When you're ready write 'Done'"
    preg = True
    while preg == True:
        for i in INV:
            buy = raw_input("Which article or articles do you want to buy?\n")
            buy = buy.lower()
            if buy == buy in INV:
                LIST.append(buy)
                print "In your shopping cart are: \n" + str(LIST)
                BILL[buy] = LIST.count(i)
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
        multy = float(LIST.count(i)) * float(PRIC[i])
        unit = LIST.count(i)
        print "Price of your " + str(unit) +" "+ i + "(s) is: ""$.""%.2f" %float(multy) +"\n"
        total = multy + total
    cards(total)


def cards(total):
    """ Here is the cards functions """
    while True:
        if "gold" in LIST or "gold card" in LIST:
            print "Invoice Subtotal is: ..................." "$" "%.2f" %float(total)
            print "The tax of IVA is:......................" "$" "%.2f" %float(total * 0.12)
            total = (total * 0.12) + total
            print "Your total with IVA is: ................" "$" "%.2f" %float(total)
            reduction = total - (total * 0.05)
            print "Our discount with gold card is:........." "$" "%.2f" %float(total*0.05)
            print "___________________________________________"
            print "Your total with discount is:............" "$" "%.2f" %float(reduction)
        elif "silver" in LIST or "silver card" in LIST:
            print "Invoice Subtotal is: ..................." "$" "%.2f" %float(total)
            print "The tax of IVA is:......................" "$" "%.2f" %float(total * 0.12)
            total = (total * 0.12) + total
            print "Your total with IVA is: ................" "$" "%.2f" %float(total)
            reduction = total - (total * 0.02)
            print "Our discount with silver card is:......." "$" "%.2f" %float(total*0.02)
            print "___________________________________________"
            print "Your total with discount is:............" "$" "%.2f" %float(reduction)
        elif "silver" in LIST and "gold" in LIST:
            print "Invoice Subtotal is: ..................." "$" "%.2f" %float(total)
            print "The tax of IVA is:......................" "$" "%.2f" %float(total * 0.12)
            total = (total * 0.12) + total
            print "Your total with IVA is: ................" "$" "%.2f" %float(total)
            reduction = total - (total * 0.05)
            print "Our discount with gold card is:........." "$" "%.2f" %float(total*0.05)
            print "___________________________________________"
            print "Your total with discount is:............" "$" "%.2f" %float(reduction)
        else:
            print "Invoice total is: ......................" "$" "%.2f" %float(total)
            print "The tax of IVA is:......................" "$" "%.2f" %float(total * 0.12)
            total = (total * 0.12) + total
            print "Your total with IVA is ................." "$" "%.2f" %float(total)
            print "You don't have a discount card.........." "$" "%.2f" %float(0)
            print "___________________________________________"
            print "The total of your invoice is:..........." "$" "%.2f" %float(total)

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
        print "The cost is " "$" "%.2f" %float(PRIC[i])
    finish()
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
                print "Error you can only insert words"
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
def out():
    """This function exits the program"""
    print "Thanks for Visit Us."
    raw_input(">>>Press Enter for Continue<<<")
    sys.exit()
def menu():
    """Here we create a menu that shows the options that user can select!"""
    while True:
        os.system("cls")
        print u""" /$$      /$$                  /$$                 /$$        """
        print u"""| $$$    /$$$                 | $$                | $$        """
        print u"""| $$$$  /$$$$ /$$$$$$  /$$$$$$| $$   /$$ /$$$$$$ /$$$$$$       """
        print u"""| $$ $$/$$ $$|____  $$/$$__  $| $$  /$$//$$__  $|_  $$_/       """
        print u"""| $$  $$$| $$ /$$$$$$| $$  \__| $$$$$$/| $$$$$$$$ | $$  __   """
        print u"""| $$\  $ | $$/$$__  $| $$     | $$_  $$| $$_____/ | $$ /$$           """
        print u"""| $$ \/  | $|  $$$$$$| $$     | $$ \  $|  $$$$$$$ |  $$$$/      """
        print u"""|__/     |__/\_______|__/     |__/  \__/\_______/  \___/      """

        print"""========================================="""
        print"""|----------------Welcome...-------------|"""
        print"""|-------Hi, here you can insert---------|"""
        print"""|-----All the products you want---------|"""
        print"""========================================="""

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
