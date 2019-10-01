# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab3_Act1_ProgE
# Date:		9/9/2019 day month year
print("Enter a value greater than 0 for miles/hour to convert it to meters/second")
Miles_hour = float(input())
End = 1
while End == 1:
    while Miles_hour < 0:
        print("Please enter a valid number")
        print("Enter a value greater than 0 for miles/hour to convert it to meters/second")
        Miles_hour = float(input())
    Seconds_hour = 3600
    Meter_mile = 1.609344 * 1000
    Meter_Sec = Miles_hour/Seconds_hour * Meter_mile
    print(Meter_Sec,"m/s")
    print("-------------")
    print("""Enter more values or to stop enter "Stop" to end program""")
    Check = str(input())
    Stop = ("Stop")
    if Check == Stop:
        End += End
        print("Program terminated")
    else:
        Miles_hour = float(Check)
        while Miles_hour < 0:
            print("Please enter a valid number")
            print("Enter a value greater than 0 for miles/hour to convert it to meters/second")
            Miles_hour = float(input())