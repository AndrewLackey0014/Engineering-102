# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab3_Act1_ProgB
# Date:		9/9/2019 day month year
print("Enter a value greater than 0 for BTU to convert it to joules")
BTU = float(input())
End = 1
while End == 1:
    while BTU < 0:
        print("Please enter a valid number")
        print("Enter a value greater than 0 for BTU to convert it to joules")
        BTU = float(input())
    Joules = 1055.05585262
    Conversion = BTU * Joules
    print(Conversion,"J")
    print("-------------")
    print("""Enter more values or to stop enter "Stop" to end program""")
    Check = str(input())
    Stop = ("Stop")
    if Check == Stop:
        End += End
        print("Program terminated")
    else:
        BTU = float(Check)
        while BTU < 0:
            print("Please enter a valid number")
            print("Enter a value greater than 0 for BTU to convert it to joules")
            BTU = float(input())