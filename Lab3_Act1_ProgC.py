# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab3_Act1_ProgC
# Date:		9/9/2019 day month year
print("Enter a value greater than 0 for pascals to convert it to mm of mercury")
Pascals = float(input())
End = 1
while End == 1:
    while Pascals < 0:
        print("Please enter a valid number")
        print("Enter a value greater than 0 for pascals to convert it to mm of mercury")
        Pascals = float(input())
    Mercury = 0.0075006156130264
    Conversion = Pascals * Mercury
    print(Conversion,"mm of hg")
    print("-------------")
    print("""Enter more values or to stop enter "Stop" to end program""")
    Check = str(input())
    Stop = ("Stop")
    if Check == Stop:
        End += End
        print("Program terminated")
    else:
        Pascals = float(Check)
        while Pascals < 0:
            print("Please enter a valid number")
            print("Enter a value greater than 0 for pascals to convert it to mm of mercury")
            Pascals = float(input())