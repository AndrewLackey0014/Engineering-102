# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab5_Act2_Prog1
# Date:		25/9/2019 day month year

# Part A
print("\nA cubic polynomial is an equation of the form Ax\N{SUPERSCRIPT THREE} + Bx\N{SUPERSCRIPT TWO} + Cx + D."
      "\nPick numbers for the coefficients of the equation which are"
      "\nA, B, C, D and the program will evaluate the derivative of the"
      "\nfunction.")
End = 1
# Loop allows the user to input coefficients
while End == 1:
    try:
        End += 1
        print()
        A = float(input("A: "))
        B = float(input("B: "))
        C = float(input("C: "))
        D = float(input("D: "))
        if A == 0 and B == 0 and C == 0 and D == 0:
            print("\nAll coefficients are 0, therefore 0 = 0 \nTry again")
            End -= 1
    except ValueError:
        print("\nPlease enter valid numbers")
        End -= 1
Derivative_A = (A * 3)
Derivative_B = (B * 2)
Derivative_C = (C * 1)
Derivative_D = (D * 0)
print("The derivative of the function is %gx\N{SUPERSCRIPT TWO} + %gx + %g" % (Derivative_A, Derivative_B, Derivative_C))
End -= 1
# Loop allows the user to input an x to be evaluated
while End == 1:
    try:
        End += 1
        print()
        print("Enter a value for x to evaluate the derivative")
        X = float(input("x:"))
    except ValueError:
        print("\nPlease enter a valid number")
        End -= 1
# Evaluation of the derivative at x
Real_Evaluation = (Derivative_A * X**2 + Derivative_B * X + Derivative_C)
print("\nThe evaluated derivative is %g" % Real_Evaluation)

#Part B
Tolerance = 1e-6
Count = 0
a = 0.1
End -= 1
# Loop gets close to the actual number within tolerance
while End == 1:
    Evaluate = (A*(X + a)**3 + B*(X + a)**2 + C*(X + a) + D - (A*X**3 + B*X**2 + C*X + D)) / a
    a = (a / 2)
    Count += 1
    if abs(Real_Evaluation - Evaluate) < Tolerance:
        End += 1
Close = abs(Evaluate - Real_Evaluation)
print("\nf'(%g) =  %g it took %g iterations and is within %g to the actual value." % (X, Evaluate, Count, Close))
