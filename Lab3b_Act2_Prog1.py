# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab3b_Act2_Prog1 (e.g. Lab 1b-2)
# Date:		11/9/2019 day month year
from math import *
Restart = 1
while Restart == 1:
    Observer = (input("Enter (X,Y,Z) point for the observer separated by commas: ")).split(",")
    for i in range(0, len(Observer)):
        Observer = [x.strip() for x in Observer] #removes spaces
        Observer = [x.strip("("+")") for x in Observer] #removes parentheses
    def Maybe_Float(Observer):
        try:
            return float(Observer)
        except (ValueError):
            Observer = [s for s in Observer if s.isdigit()]
    New_observer = [Maybe_Float(i) for i in Observer] #creates a None value where a string is (using the def statement)
    New_observer = list(filter(None.__ne__,New_observer)) #gets rid of None value
    if len(New_observer) > 3: #checks validity of point
        print("Invalid point")
        print("Try again")
    elif len(New_observer) < 3: #checks validity of point
        print("Invalid point")
        print("Try again")
    else:
        print(New_observer,"Observer")
        Restart += Restart
Position_observer_X = New_observer[0]
Position_observer_Y = New_observer[1]
Position_observer_Z = New_observer[2]
Restart = 1
while Restart == 1:
    First_point = (input("Enter (X,Y,Z) point for the first observed point separated by commas: ")).split(",")
    for i in range(0, len(First_point)):
        First_point = [x.strip() for x in First_point] #removes spaces
        First_point = [x.strip("("+")") for x in First_point] #removes parentheses
    def Maybe_Float(First_point):
        try:
            return float(First_point)
        except (ValueError, TypeError):
            First_point = [s for s in First_point if s.isdigit()]
    New_first = [Maybe_Float(i) for i in First_point] #creates a None value where a string is (using the def statement)
    New_first = list(filter(None.__ne__, New_first)) #gets rid of None value
    if len(New_first) > 3: #checks validity of point
        print("Invalid point")
        print("Try again")
    elif len(New_first) < 3: #checks validity of point
        print("Invalid point")
        print("Try again")
    else:
        print(New_first,"First point")
        Restart += Restart
Position_first_X = New_first[0]
Position_first_Y = New_first[1]
Position_first_Z = New_first[2]
Distance_first_X = (Position_observer_X - Position_first_X)
Distance_first_Y = (Position_observer_Y - Position_first_Y)
Distance_first_Z = (Position_observer_Z - Position_first_Z)
Restart = 1
while Restart == 1:
    Second_point = (input("Enter (X,Y,Z) point for the second observed point separated by commas: ")).split(",")
    for i in range(0, len(Second_point)):
        Second_point = [x.strip() for x in Second_point] #removes spaces
        Second_point = [x.strip("("+")") for x in Second_point] #removes parentheses
    def Maybe_Float(Second_point):
        try:
            return float(Second_point)
        except (ValueError, TypeError):
            Second_point = [s for s in Second_point if s.isdigit()]
    New_second = [Maybe_Float(i) for i in Second_point] #creates a None value where a string is (using the def statement)
    New_second = list(filter(None.__ne__, New_second)) #gets rid of None value
    if len(New_second) > 3: #checks validity of point
        print("Invalid point")
        print("Try again")
    elif len(New_second) < 3: #checks validity of point
        print("Invalid point")
        print("Try again")
    else:
        print(New_second,"Second point")
        Restart += Restart
Position_second_X = New_second[0]
Position_second_Y = New_second[1]
Position_second_Z = New_second[2]
Distance_second_X = (Position_observer_X - Position_second_X)
Distance_second_Y = (Position_observer_Y - Position_second_Y)
Distance_second_Z = (Position_observer_Z - Position_second_Z)
#normalization and calculation of the angle in 3D
Normalize_first = sqrt(Distance_first_X**2 + Distance_first_Y**2 + Distance_first_Z**2)
Normalize_second = sqrt(Distance_second_X**2 + Distance_second_Y**2 + Distance_second_Z**2)
print(Normalize_first) #CHECK
print(Normalize_second) #CHECK
First_Second_Normalization = (Position_first_X * Position_second_X) + (Position_first_Y * Position_second_Y) + (Position_first_Z * Position_second_Z)
print(First_Second_Normalization) #CHECK
Cos_angle = First_Second_Normalization / (Normalize_first * Normalize_second)
print(Cos_angle) #CHECK
print((acos(Cos_angle)*180)/pi,"Degrees")