# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab3b_Act1_Prog1D (e.g. Lab 1b-2)
# Date:		11/9/2019 day month year
print("""Enter in numbers to calculate the standard deviation, type "Stop" when done""")
try:
    User_list = []
    while True:
        User_list.append(float(input()))
except ValueError:
    print(User_list)
print("----------")
len(User_list)
Average = sum(User_list) / len(User_list)
Count = 0
Add_Sum_of = 0
while len(User_list) > Count:
    Sum_of = (User_list[0 + Count] - Average)**2
    Count += 1
    Add_Sum_of += Sum_of
Standard_dev = ((Add_Sum_of)/(len(User_list) - 1))**(1/2)
print(Standard_dev,"standard deviation for the numbers",User_list)