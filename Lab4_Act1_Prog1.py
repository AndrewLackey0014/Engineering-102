# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab4_Act1_Prog1
# Date:		16/9/2019 day month year
a = 1/7
print(a)
b = a*7 #1
print(b)
print()

a = 1/7
print(a)
b = 7*a #1
print(b)
c = 2*a #2/7
d = 5*a #5/7
e = c+d #7/7
print(e)
print()

from math import *
x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)
print()

# define tolerance
TOL = 1e-10
a = 1/7
print(a)
b = 7*a #1
print(b)
c = 2*a #2/7
d = 5*a #5/7
e = c+d #7/7
print(e)
# check if b and e are equal within specified tolerance
if (abs(b-e)) < TOL:
    print('b and e are equal within tolerance of', TOL)
else:
    print('b and e are NOT equal within tolerance of', TOL)
print()

from math import *
TOL = 1e-10
x = sqrt(1/3)
print(x)
y = x*x*3 #1
print(y)
z = x*3*x
print(z)
#check if y and z are equal within specific tolerance
if (abs(z-y)) < TOL:
    print('y and z are equal within tolerance of',TOL)
else:
    print('y and z are NOT equal within tolerance of',TOL)
print()
