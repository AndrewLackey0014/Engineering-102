# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab3_Act1_ProgF
# Date:		9/9/2019 day month year
print("Enter a value for temperature in fahrenheit to convert it to celsius")
Fahrenheit = float(input())
End = 1
while End == 1:
    while Fahrenheit < -459.670:
        print("Please enter a valid number")
        print("Enter a value for temperature in fahrenheit to convert it to celsius")
        Fahrenheit = float(input())
    Celcius = (Fahrenheit - 32) * (5/9)
    print(Celcius,"C")
    print("-------------")
    print("""Enter more temperatures or to stop enter "Stop" to end program""")
    Check = str(input())
    Stop = ("Stop")
    if Check == Stop:
        End += End
        print("Program terminated")
    else:
        Fahrenheit = float(Check)
        while Fahrenheit < -459.670:
            print("Please enter a valid number")
            print("Enter a value for temperature in fahrenheit to convert it to celsius")
            Fahrenheit = float(input())