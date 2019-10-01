# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab5_Act2_Prog2_Andrew (e.g. Lab 1b-2)
# Date:		25/9/2019 day month year
from math import *
print("\nEnter a number to evaluate the derivative of sin(x) at that number")
End = 1
# Loops allows the user to input the number for x
while End == 1:
    try:
        End += 1
        print()
        X = float(input("X: "))
    except ValueError:
        print("\nPlease enter valid numbers")
        End -= 1
Tolerance = 1e-6
Count = 0
a = 0.1
End -= 1
# Does the calculations until the answer is close to the actual answer
while End == 1:
    Evaluate = (sin(X + a) - sin(X)) / a
    a = (a / 2)
    Count += 1
    if abs(Evaluate - cos(X)) <= Tolerance:
        End += 1
print("The computed derivative of sin(x) at value of %g is %g"
      "\nand it took %g iterations to the computation" % (X, Evaluate, Count))
