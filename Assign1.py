"""
Name: Julia Anantchenko
Class: 1026A - Computer Science Fundamentals I
Teacher: Michael A. Bauer
Date: October 2nd 2019
Program Description: Computes the cost of breakfast at the Good Morning America! restaurant.
"""

# food price constants
EGG = 0.99
BACON = 0.49
SAUSAGE = 1.49
HASH_BROWN = 1.19
TOAST = 0.79
COFFEE = 1.09
TEA = 0.89
SMALL_BREAKFAST = EGG + HASH_BROWN + 2*TOAST + 2*BACON + SAUSAGE
REGULAR_BREAKFAST = 2*EGG + HASH_BROWN + 2*TOAST + 4*BACON + 2*SAUSAGE
BIG_BREAKFAST = 3*EGG + 2*HASH_BROWN + 4*TOAST + 6*BACON + 3*SAUSAGE

# variables for counting the cost and the food chosen
totalFoodCost = 0
foodChoice = ""

# function provided by assignment, formats input
def formatInput (textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine


# while loop for receiving order and counting total, continues until q is entered
while True:

    # prompts for food choice input and formats it
    foodChoice = formatInput(input("Enter item (q to terminate): small breakfast, regular breakfast, " +
                                   "big breakfast, egg, \nbacon, sausage, hash brown, toast, coffee, tea: "))

    # shows order total if q is entered
    if foodChoice == "q":
        break

    # checks for valid input
    if foodChoice == "small breakfast" or foodChoice == "regular breakfast" or foodChoice == "big breakfast" \
            or foodChoice == "egg" or foodChoice == "bacon" or foodChoice == "sausage" or foodChoice == "hash brown" \
            or foodChoice == "toast" or foodChoice == "coffee" or foodChoice == "tea":

        # prompts for quantity of food
        quantity = input("Enter quantity: ")

        # checks for valid input & converts to int
        if quantity.isnumeric():
            quantity = int(quantity)

            # adds order to the total food cost
            if foodChoice == "small breakfast":
                totalFoodCost += quantity*SMALL_BREAKFAST
            if foodChoice == "regular breakfast":
                totalFoodCost += quantity*REGULAR_BREAKFAST
            if foodChoice == "big breakfast":
                totalFoodCost += quantity*BIG_BREAKFAST
            if foodChoice == "egg":
                totalFoodCost += quantity*EGG
            if foodChoice == "bacon":
                totalFoodCost += quantity*BACON
            if foodChoice == "sausage":
                totalFoodCost += quantity*SAUSAGE
            if foodChoice == "hash brown":
                totalFoodCost += quantity*HASH_BROWN
            if foodChoice == "toast":
                totalFoodCost += quantity*TOAST
            if foodChoice == "coffee":
                totalFoodCost += quantity*COFFEE
            if foodChoice == "tea":
                totalFoodCost += quantity*TEA

        # tells user if quantity is invalid
        else:
            print("Invalid quantity. Try again.")

    # tells user if food choice is invalid
    else:
        print("Invalid food choice. Try again.")


# prints total prices
print("\n%-10s%7s" % ("Cost :", ("$%.2f" % totalFoodCost)), "\n%-10s%7s"
      % ("Tax : ", "$%.2f" % (totalFoodCost*0.13)), "\n%-10s%7s"
      % ("Total : ", "$%.2f" % (totalFoodCost*1.13)))
