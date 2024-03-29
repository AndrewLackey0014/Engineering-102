# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab 1b-2 (e.g. Lab 1b-2)
# Date:		29/8/2019 day month year
from math import *
print()
print("This shows the evaluation of 5*x/(x-2) evaluated close to x=1")
print()
print(5*1.1/(1.1-2))
print(5*1.01/(1.01-2))
print(5*1.001/(1.001-2))
print(5*1.0001/(1.0001-2))
print(5*1.00001/(1.00001-2))
print(5*1.000001/(1.000001-2))
print(5*1.0000001/(1.0000001-2))
print(5*1.00000001/(1.00000001-2))
print()
print("this shows the evaluation of sin(x)/x as x gets closer to 0")
print()
print(sin(1)/1)
print(sin(.1)/.1)
print(sin(.01)/.01)
print(sin(.001)/.001)
print(sin(.0001)/.0001)
print(sin(.00001)/.00001)
print(sin(.000001)/.000001)
print(sin(.0000001)/.0000001)
print()
print("this shows the evaluation of 1-cos(x)/x**2 as x gets closer to 0")
print()
print((1-cos(1))/1**2)
print((1-cos(.1))/.1**2)
print((1-cos(.01))/.01**2)
print((1-cos(.001))/.001**2)
print((1-cos(.0001))/.0001**2)
print((1-cos(.00001))/.00001**2)
print((1-cos(.000001))/.000001**2)
print((1-cos(.0000001))/.0000001**2)
print()
print("this shows the evaluation of (1+1/x)**x as x ranges from 1 to 10**7 evaluating every 10 times")
print()
print((1+(1/1))**1)
print((1+(1/10))**10)
print((1+(1/100))**100)
print((1+(1/1000))**1000)
print((1+(1/10000))**10000)
print((1+(1/100000))**100000)
print((1+(1/1000000))**1000000)
print((1+(1/10000000))**10000000)