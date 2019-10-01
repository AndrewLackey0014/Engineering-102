# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab3b_Act1_Prog1A (e.g. Lab 1b-2)
# Date:		10/9/2019 day month year
End = 1
print("To find kinetic Energy of an object")
print("Enter Mass in kg")
Mass = float(input())
print("Enter Velocity in m/s")
Velocity = float(input())
Kinetic_E = ( 1 / 2 ) * Mass * Velocity ** 2
print(Kinetic_E, "J")
print("-----------")
while End == 1:
    print("""Are you done? Enter "Yes" if so or enter "No" to continue.""")
    Check = str(input())
    Yes = ("Yes")
    if Check == Yes:
        End += End
        print("Program terminated")
    else:
        print("Enter Mass in kg")
        Mass = float(input())
        print("Enter Velocity in m/s")
        Velocity = float(input())
        Kinetic_E = (1 / 2) * Mass * Velocity ** 2
        print(Kinetic_E, "J")
        print("-----------")