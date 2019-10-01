# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Daniel Sanchez
#			Kevin Swedlund
# Section:		533
# Assignment:	Lab2_Act3_Prog1
# Date:		5/9/2019 day month year
Distance_1 = 50 #meters of first measurment
Distance_2 = 615 #meters of second measurment
Time_1 = 30 #seconds of first measurment
Time_2 = 45 #seconds of second measurment
Velocity = (Distance_2-Distance_1)/(Time_2-Time_1)
print("Enter time between 30 and 45 seconds.")
Time_2 = float(input()) #time you want to know the location at input in console
Distance = ((Time_2-Time_1)*Velocity)
Meters_past = Distance+50 #distance of the car on the track with reference to the starting line
while Time_2 < 30:
    print("Please pick time between 30 and 45 seconds")
    Time_2 = float(input())
while Time_2 > 45:
    print("Please pick time between 30 and 45 seconds")
    Time_2 = float(input())
if 30 <= Time_2 <= 45:
    Distance = ((Time_2 - Time_1) * Velocity)
    Meters_past = Distance + 50  # distance of the car on the track with reference to the starting line
    print(Meters_past,"meters past the starting line")
    print("location of the car at time",Time_2,"seconds")
