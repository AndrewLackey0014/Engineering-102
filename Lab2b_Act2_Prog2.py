# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab2b_Act2_Prog2 (e.g. Lab 1b-2)
# Date:		8/9/2019 day month year
Time_1 = 13
Time_2 = 84
Start_position_X = 1
Start_position_Y = 3
Start_position_Z = 7
End_position_X = 23
End_position_Y = -5
End_position_Z = 10
Velocity_x = (End_position_X - Start_position_X)/(Time_2-Time_1)
Velocity_y = (End_position_Y - Start_position_Y)/(Time_2-Time_1)
Velocity_z = (End_position_Z - Start_position_Z)/(Time_2-Time_1)
print("Enter a time value greater than 0 seconds")
New_time = float(input())
while New_time < 0:
    print("Please input a valid time")
    print("Enter a time value greater than 0 seconds")
    New_time = float(input())
Repeat = 0
while Repeat < 5: #Gives 5 consecutive times +1 of user input
    New_x = (Velocity_x * (New_time - 13)) + Start_position_X
    New_y = (Velocity_y * (New_time - 13)) + Start_position_Y
    New_z = (Velocity_z * (New_time - 13)) + Start_position_Z
    print("at time value",New_time,"seconds the position of the point is")
    print("X = ",New_x,"m")
    print("Y = ",New_y,"m")
    print("Z = ",New_z,"m")
    print("------------------")
    Repeat += 1
    New_time += 1