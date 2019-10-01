# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab4b_Act1_Prog2 (e.g. Lab 1b-2)
# Date:		17/9/2019 day month year
print("Input all numbers asked to receive the Reynolds Number of ")
End = 1
while End == 1:
    try:
        Velocity = float(input("\nEnter the characteristic velocity of the flow in m/s: "))
        End += 1
    except ValueError:
        print("Please input a valid number\n")
while End == 2:
    try:
        Diameter = float(input("\nEnter in the diameter of the pipe in m: "))
        End += 1
    except ValueError:
        print("Please input a valid number\n")
while End == 3:
    try:
        Kinematic_viscosity = float(input("\nEnter in the fluid kinematic viscosity in m^2/s: "))
        End += 1
    except ValueError:
        print("Please input a valid number\n")
Calculate = (Velocity*Diameter)/Kinematic_viscosity
print()
if Calculate < 2300:
    print(Calculate, "\nthe flow is laminar.")
elif Calculate > 2900:
    print(Calculate, "\nthe flow is turbulent.")
else:
    print(Calculate, "\nthe flow is in transition.")