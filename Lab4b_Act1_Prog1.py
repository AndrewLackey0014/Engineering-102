# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab4b_Act1_Prog1 (e.g. Lab 1b-2)
# Date:		16/9/2019 day month year
print("This program takes a list of numbers given and gives the biggest value back \nor puts the list in numerical order")
User_list = input("Enter as many numbers as you want separated by commas: ").split(",")
for i in range(0, len(User_list)):
    User_list = [x.strip() for x in User_list]  # removes spaces
def Maybe_Float(User_list):
    try:
        return float(User_list) #converts string to float in the list
    except (ValueError):
        User_list = [s for s in User_list if s.isdigit()]
New_list = [Maybe_Float(i) for i in User_list]  # creates a None value where a string is (using the def statement)
New_list = list(filter(None.__ne__, New_list))  # gets rid of None value
print(New_list,"\nThe initial list")
End = 1
while End == 1:
    print("\nWhat would you like to find? The sorted list or the largest value?")
    Question = input("""\nEnter "Sort" to sort the list or "Value" to get the largest value: """).strip()
    if Question == "Sort":
        New_list.sort()
        print(New_list, "\nThe new list in numerical order")  # gives the sorted list
        End = 2
    elif Question == "Value":
        print(max(New_list), "Is the highest value in the list")  # finds the largest value in the list
        End = 2
    else:
        print("""\nPlease answer the question with either "Sort" or "Value" """)
# I didn't really need lines 21-33 they are in here just for the if-elif-else statments. Better way to do it is print(max(New_list)) if you want the largest value
# Or if you want to sort the list in numerical order you can just do New_list.sort() then print(New_list)