# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab4b_Act1_Prog3 (e.g. Lab 1b-2)
# Date:		17/9/2019 day month year
print("This program looks at a machine that for the first 10 days only produces"
      "\n10 widgets per day, then starts producing at full speed making 40 per"
      "\nday for 50 days. After those 50 days it starts slowing down by one"
      "\nwidget per day until it eventually stops. When you input a number of days"
      "\nthe program will tell you how many widgets the machine has made up to that"
      "\npoint")
End = 1
while End == 1:
    try:
        Days = int(input("\nEnter a number for days: "))
        End += 1
        if Days < 0:
            print("\nCannot have negative days"
                  "\nPlease try again")
            End -= 1
    except ValueError:
        print("\nPlease input a valid number")
if Days <= 10:
    Widgets = Days * 10
    print(Widgets, "widgets were produced over", Days, "days")
elif 10 < Days <= 60:
    Widgets = 100 + ((Days-10) * 40)
    print(Widgets, "widgets were produced over", Days, "days")
elif 60 < Days <= 100:
    X = Days - 60
    Widgets = 2100  # Number taken from previous step
    while X > 0:  # Loop to take the new days and calculate the widgets made as it starts decreasing production
        Created_Day = (40 - X)  # Number of widgets produced on the new day as its decreasing production
        Widgets += Created_Day  # Offloads the widgets to a saved variable in the loop
        X -= 1
    print(Widgets, "widgets were produced over", Days, "days")
else:
    Widgets = 2880
    print(Widgets, "widgets were produced over", Days, "days")