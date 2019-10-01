# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab3_Act1_ProgD
# Date:		9/9/2019 day month year
print("Enter a value greater than 0 for seconds/revolution to convert it to hertz")
Sec_rev = float(input())
End = 1
while End == 1:
    while Sec_rev < 0:
        print("Please enter a valid number")
        print("Enter a value greater than 0 for seconds/revolution to convert it to hertz")
        Sec_rev = float(input())
    Hertz = 1/Sec_rev
    print(Hertz,"Hz")
    print("-------------")
    print("""Enter more values or to stop enter "Stop" to end program""")
    Check = str(input())
    Stop = ("Stop")
    if Check == Stop:
        End += End
        print("Program terminated")
    else:
        Sec_rev = float(Check)
        while Sec_rev < 0:
            print("Please enter a valid number")
            print("Enter a value greater than 0 for seconds/revolution to convert it to hertz")
            Sec_rev = float(input())