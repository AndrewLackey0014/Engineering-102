# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab5_Act1_Prog1
# Date:		23/9/2019 day month year

# Test 1x**3 - 5x**2 - 6x - 0 =0 , roots [0, 6, -1] bounds can only contain one root
# Test 1x**3 - 4x**2 - 7x + 10 = 0 , roots [1, 5, -2] bounds can only contain one root
# Test 1x**3 + 3x**2 - 6x - 18 = 0 , roots [-3, sqrt6, -sqrt6] bounds can only contain one root
# Test 1x**3 - 7x**2 + 4x + 12 = 0 , roots [6, 2, -1] bounds can only contain one root

Counter = 0
# Used numby instead of bisections which was given the green light by professor Brooks
import numpy as np
print("\nA cubic polynomial is an equation of the form Ax\N{SUPERSCRIPT THREE} + Bx\N{SUPERSCRIPT TWO} + Cx + D = 0."
      "\nPick numbers for the coefficients of the equation which are"
      "\nA, B, C, D and the program will evaluate the roots of the equation."
      "\nYou will also need to restrict the domain for the program to evaluate the "
      "\nroot in the domain.")
End = 1
# Loop allows the user to select the coefficients
while End == 1:
    try:
        End += 1
        print()
        A = float(input("A: "))
        B = float(input("B: "))
        C = float(input("C: "))
        D = float(input("D: "))
        if A == 0 and B == 0 and C == 0 and D != 0:
            print("\nValue error %g = 0" % D, "\nTry again")
            End -= 1
        elif A == 0 and B == 0 and C == 0 and D == 0:
            print("\nAll coefficients are 0, therefore 0 = 0 \nTry again")
            End -= 1
        Coeff = [A, B, C, D]
    except ValueError:
        print("\nPlease enter valid numbers")
        End -= 1
Roots = np.roots(Coeff)
Real_roots = Roots.real[abs(Roots.imag) < 1e-6]  # Tolerates imaginary of 1e-6
print("\nInput a restriction on the domain such that values of A and B, with B >= A+1."
      "\nPlease use whole numbers for the restriction.")
End -= 1
# Loop checks validity of the domain restriction
while End == 1:
    # Loop allows user to restrict the domain
    while End == 1:
        try:
            End += 1
            print()
            Domain_1 = int(input("A: "))
            Domain_2 = int(input("B: "))
            if Domain_1 >= Domain_2:
                print("\nPlease enter a valid domain")
                End -= 1
            elif (Domain_2 - Domain_1) < 1:
                print("\nDomain restriction does not fit parameters try again (B >= A+1)")
                End -= 1
        except ValueError:
            print("\nPlease enter a valid domain")
            End -= 1
    Counter += 1
    Domain = [Domain_1,Domain_2]
    # Checks if the polynomial has one real root and does checks to make sure its in the restriction
    if len(Real_roots) == 1:
        for x in range(1):
            if Domain_1 < Real_roots[0] < Domain_2:
                print("\nRoot with restricted domain x = %g" % Real_roots[0], ", Domain: %s" % Domain,
                      "\nIt took %g iteration(s) to get the answer" % Counter)
            else:
                print("\nNo roots found at domain restriction."
                      "\nEnter a new restriction on the domain.")
                End -= 1
    # Checks if the polynomial has two real roots and does checks to make sure its in the restriction
    if len(Real_roots) == 2:
        for x in range(1):
            if Domain_1 < Real_roots[0] < Domain_2 and Domain_1 < Real_roots[1] < Domain_2:
                print("\nDomain contains two roots please further restrict the domain")
                End -= 1
                break
            if Domain_1 < Real_roots[0] < Domain_2:
                print("\nRoot with restricted domain x = %g" % Real_roots[0], ", Domain: %s" % Domain,
                      "\nIt took %g iteration(s) to get the answer" % Counter)
            elif Domain_1 < Real_roots[1] < Domain_2:
                print("\nRoot with restricted domain x = %g" % Real_roots[1], ", Domain: %s" % Domain,
                      "\nIt took %g iteration(s) to get the answer" % Counter)
            else:
                print("\nNo roots found at domain restriction."
                      "\nEnter a new restriction on the domain.")
                End -= 1
    # Checks if the polynomial has three real roots and does checks to make sure its in the restriction
    if len(Real_roots) == 3:
        for x in range(1):
            if Domain_1 < Real_roots[0] < Domain_2 and Domain_1 < Real_roots[1] < Domain_2 or\
                    Domain_1 < Real_roots[0] < Domain_2 and Domain_1 < Real_roots[2] < Domain_2 or\
                    Domain_1 < Real_roots[1] < Domain_2 and Domain_1 < Real_roots[2] < Domain_2:
                print("\nDomain contains multiple roots please further restrict the domain")
                End -= 1
                break
            if Domain_1 < Real_roots[0] < Domain_2:
                print("\nRoot with restricted domain x = %g" % Real_roots[0], ", Domain: %s" % Domain,
                      "\nIt took %g iteration(s) to get the answer" % Counter)
            elif Domain_1 < Real_roots[1] < Domain_2:
                print("\nRoot with restricted domain x = %g" % Real_roots[1], ", Domain: %s" % Domain,
                      "\nIt took %g iteration(s) to get the answer" % Counter)
            elif Domain_1 < Real_roots[2] < Domain_2:
                print("\nRoot with restricted domain x = %g" % Real_roots[2], ", Domain: %s" % Domain,
                      "\nIt took %g iteration(s) to get the answer" % Counter)
            else:
                print("\nNo roots found at domain restriction."
                      "\nEnter a new restriction on the domain.")
                End -= 1
