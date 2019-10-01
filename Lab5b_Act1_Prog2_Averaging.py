# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab5b_Act1_Prog2 (e.g. Lab 1b-2)
# Date:		24/9/2019 day month year
print("\nThis program takes data entered by the user and outputs "
      "\nthe max, min, and the average of the numbers."
      "\n\nHow to input your data: "
      "\nEnter your numbers one by one hitting enter after each number."
      "\nOnce you are done add a negative to the last number you enter")
Get_average = 0  # Creating the variable
Setting_minmax = 1  # Triggers the if statement to select the starting min and max values
Average = 0  # Creating the variable
Counter = 0  # Creating the variable
End = 1  # Puts the program into the first loop
Check = 1  # Puts the program into the second loop
while End == 1:  # First loop
    while Check == 1:  # Second loop
        try:
            Check += 1  # Ends the second loop
            User_input = float(input("\nEnter your numbers hitting enter after each one: "))
            if Setting_minmax == 1:
                Min = User_input  # Sets initial min value
                Max = User_input  # Sets initial max value
                Setting_minmax += 1  # Makes it so the program can't override the max and min
            if User_input == 0:  # Detects invalid input
                print("\nCannot have a measurement of 0"
                      "\nTry again")
        except ValueError:  # Detects invalid input
            print("\nPlease input a valid measurement")
            Check -= 1  # Puts the program back into the second loop
    if User_input < 0:  # Detects for negative numbers
        End += 1  # Ends the first loop
        User_input = abs(User_input)  # Turns the negative number to positive
        Get_average += 1  # Allows the program to take the average
    if Max < User_input:  # Detects for a new max
        Max = User_input  # Sets new max
    if Min > User_input:  # Detects for a new min
        Min = User_input  # Sets new min
    Counter += 1  # Counts how many times the loop is made for the average
    Average += User_input  # Adds all the user input together to get the first part of an average
    Check -= 1  # Puts the program back in the second loop
    if Get_average == 1:  # Gets the average and prints all the statements when true
        Average = (Average / Counter)  # Gets the final result of the average
        print("\nYou entered a total of %g numbers"
              "\nThe maximum number is %g"
              "\nThe minimum number is %g"
              "\nWhile the average of all the numbers is %g" % (Counter, Max, Min, Average))



