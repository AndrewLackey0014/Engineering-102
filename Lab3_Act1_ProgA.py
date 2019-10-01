# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab3_Act1_ProgA
# Date:		9/9/2019 day month year
print("Enter a value greater than 0 for pounds to convert it to Newtons")
Pounds = float(input())
End = 1
while End == 1:
    while Pounds < 0:
        print("Please enter a valid number")
        print("Enter a value greater than 0 for pounds to convert it to Newtons")
        Pounds = float(input())
    Mass_kg = Pounds * 0.45359237
    Newtons = Mass_kg * 9.81
    print(Newtons,"N")
    print("-------------")
    print("""Enter more values or to stop enter "Stop" to end program""")
    Check = str(input())
    Stop = ("Stop")
    if Check == Stop:
        End += End
        print("Program terminated")
    else:
        Pounds = float(Check)
        while Pounds < 0:
            print("Please enter a valid number")
            print("Enter a value greater than 0 for pounds to convert it to Newtons")
            Pounds = float(input())
