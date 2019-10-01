# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab2_Act3_Prog2
# Date:		5/9/2019 day month year
from math import *
Radius = 1 #km
Full_rotation = (2*pi*Radius) #circumference
print("Pick Velocity between 1 and 6 km/min")
Velocity = float(input())
while Velocity > 6 or Velocity < 1:
    print("Invalid Answer")
    print("Pick Velocity between 1 and 6 km/min")
    Velocity = float(input())
Halfway = (1/2)*Full_rotation
print("Enter time value in minutes to see location of car on circular track with reference to the starting line")
Time = float(input()) #Time you want to see car at with respect to start point
Arc_length = Velocity*Time
while Arc_length > Full_rotation: #Determine if the car has made a full rotation of the track
    Arc_length -= Full_rotation
if Arc_length <= Halfway: #Determines whether the car is before the halfway point
    print(Arc_length,"km")
else: #Determine whether the car is after the halfway point
    print(abs(Arc_length-Full_rotation),"km")
print("Location of car around the track at time",Time,"minutes")