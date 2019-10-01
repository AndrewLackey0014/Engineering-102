# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab3b_Act1_Prog1B (e.g. Lab 1b-2)
# Date:		10/9/2019 day month year
End = 1
print("To find the Reynolds Number of a fluid")
print("Enter Density in Kg/m^3")
Density = float(input())
print("Enter Velocity in m/s")
Velocity = float(input())
print("Enter Kinematic Viscosity in Ns/m^2")
Kinematic_viscosity = float(input())
print("Enter Characteristics Linear Dimensions in meters")
Linear_d = float(input())
Reynolds_number = (Density * Velocity * Linear_d) / Kinematic_viscosity
print(Reynolds_number,"lamimar flow")
print("----------")
while End == 1:
    print("""Are you done? Enter "Yes" if so or enter "No" to continue.""")
    Check = str(input())
    Yes = ("Yes")
    if Check == Yes:
        End += End
        print("Program terminated")
    else:
        print("Enter Density in Kg/m^3")
        Density = float(input())
        print("Enter Velocity in m/s")
        Velocity = float(input())
        print("Enter Kinematic Viscosity in Ns/m^2")
        Kinematic_viscosity = float(input())
        print("Enter Characteristics Linear Dimensions in meters")
        Linear_d = float(input())
        Reynolds_number = (Density * Velocity * Linear_d) / Kinematic_viscosity
        print(Reynolds_number, "lamimar flow")
        print("----------")