# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab3_Act1_ProgG
# Date:		9/9/2019 day month year
from math import *
print("Enter a value for output voltage and input voltage to calculate voltage gain in Decibel Volts")
Output_V = float(input())
Input_v = float(input())

while Input_v <= 0 :
    print("Please enter a valid number")
    print("Enter a value for the Input Voltage")
    Input_v = float(input())
while Output_V < 0 :
    print("Please enter a valid number")
    print("Enter a value for the Output Voltage")
    Output_V = float(input())
Decibel = 20*log10(Output_V / Input_v)
print(Decibel,"dB")