# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab5b_Act1_Prog3 (e.g. Lab 1b-2)
# Date:		24/9/2019 day month year
print("\nThis program evaluates the divisors of numbers from 2 to 51")
End = 1
# While statement for hitting enter to start the program
while End == 1:
    try:
        End += 1
        Go = input("\nPress enter when you are ready to run: ")
        if Go != "":
            print("\nPlease hit enter")
            End -= 1
    except ValueError:
        print("\nPlease hit enter")
        End -= 1
# Reads if enter is pressed and runs the for loops
if Go == "":
    for y in range(2,52):
        for x in range(2,52):
            if x > y:
                break
            Z = y % x
            if Z == 0:
                print("%g divides %g" % (x, y))
