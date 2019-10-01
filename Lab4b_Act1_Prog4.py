# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab4b_Act1_Prog3 (e.g. Lab 1b-2)
# Date:		17/9/2019 day month year
from math import *
import cmath
print("\nA quadratic equation is an equation of the form Ax\N{SUPERSCRIPT TWO} + Bx + C = 0."
      "\nPick numbers for the coefficients of the equation which are"
      "\nA, B, and C and the program will evaluate the roots of the equation.")
End = 1
while End == 1:
    try:
        End += 1
        print()
        A = float(input("A: "))
        B = float(input("B: "))
        C = float(input("C: "))
        if A == 0 and B == 0 and C != 0:
            print("\nValue error %g = 0" % C, "\nTry again")
            End -= 1
        elif A == 0 and B == 0 and C == 0:
            print("\nAll numbers are 0, therefore 0 = 0 \nTry again")
            End -= 1
    except ValueError:
        print("\nPlease enter valid numbers")
        End -= 1
if A != 0:
    Quadratic = B ** 2 - 4 * A * C
    if Quadratic > 0:
        X1 = (((-B) + sqrt(Quadratic)) / (2*A))
        X2 = (((-B) - sqrt(Quadratic)) / (2*A))
        print("\nThe equation has two roots X = %g and X = %g" % (X1, X2))
    elif Quadratic == 0:
        X = (-B) / (2*A)
        print("\nThe equation has one root X =", X)
    else:  # Solves the imaginary
        # Python natively supports "j" as the unit for imaginary unit instead of "i" so this program uses "j"
        X1 = ((-B + cmath.sqrt(Quadratic)) / (2*A))
        X2 = ((-B - cmath.sqrt(Quadratic)) / (2*A))
        print("\nThe equation has two complex roots X = %s and X = %s" % (X1, X2))
elif A == 0:
    if C != 0 and B != 0:
        X = (-C) / (B)
        print("\nThe equation has one root", X)
    elif C == 0 and B != 0:
        X = (C) / (B)
        print("\nThe equation has one root", X)
