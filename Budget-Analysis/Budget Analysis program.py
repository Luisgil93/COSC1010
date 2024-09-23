#
# Name Luis Gil
# Date 09/22/2024
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Variables for this code. 
userBudget= float( input("Enter how much you've budgeted for the month: "))

moreExpenses = "y"
userTotalExpenses = 0
# Where user types in thier budget amount.
while moreExpenses == "y":
    userExpenses = float(input("enter an expense: "))
    userTotalExpenses += userExpenses
# If user has more expenses they would like to add.
    moreExpenses = input("Do you have more Expenses?: Type y for yes, Any key for no: ")
 # If user is over their budget they will get this message. 
if userTotalExpenses > userBudget:
    print("You were over your budget of","$"+format(userBudget,",.2f"),"by","$"+format(userTotalExpenses - userBudget,",.2f"))
# If user is under their buget they will get this message.
elif userBudget > userTotalExpenses:
    print("You were under your budget of","$"+format(userBudget,",.2f"),"by","$"+format(userBudget - userTotalExpenses,",.2f"))
# If user has used thier exact budget they will get this message.
else:
    print("you've used your exact budget of","$"+format(userBudget,",.2f"),".")
    