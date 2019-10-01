# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab3_Act3_Prog1
# Date:		12/9/2019 day month year
#name of street
#activity
#Favorite car
#favorite food
#Outfit
#number
Street = input("Enter a name of a street: ")
Activity = input("Enter an activity: ")
Car = input("Enter your favorite car: ")
Food = input("Enter your favorite food: ")
Outfit = input("Enter an outfit: ")
Number = (input("Enter a number: "))
Change_number = float(Number)*23.11
print("\tSuddenly you wake up wearing a "+Outfit+" and craving "+Food+"."
    "\nYou walk outside to find "+Car+" and decide to drive and get "+Food+"."
    "\nWhile you are cruising down "+Street+" a crazy man jumps out in front of you."
    "\nHe challenges you in "+Activity+" and says \"I wont let you pass till you beat me "+Number+" times.\""
    "\n\"or you can pay me $",(Change_number),"\""
    "\nYou decide to give in his game and after a long fight you finally beat him",Number,"Times."
    "\nYou are finally able to get your "+Food+".")
