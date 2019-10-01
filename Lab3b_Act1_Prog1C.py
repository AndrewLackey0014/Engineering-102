# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab3b_Act1_Prog1C (e.g. Lab 1b-2)
# Date:		11/9/2019 day month year
End = 1
print("To calculate moment of inertia of a rectangular object")
print("Enter Rectangles base in meters")
Base = float(input())
print("Enter Rectangles height in meters")
Height = float(input())
Moment_inertia = (Base * Height ** 3)/ 12
print(Moment_inertia,"Kg/m^2")
print("--------")
while End == 1:
    print("""Are you done? Enter "Yes" if so or enter "No" to continue.""")
    Check = str(input())
    Yes = ("Yes")
    if Check == Yes:
        End += End
        print("Program terminated")
    else:
        print("Enter Rectangles base in meters")
        Base = float(input())
        print("Enter Rectangles height in meters")
        Height = float(input())
        Moment_inertia = (Base * Height ** 3) / 12
        print(Moment_inertia, "Kg/m^2")
        print("--------")
