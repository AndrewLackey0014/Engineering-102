# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab3_Act2_Prog1
# Date:		11/9/2019 day month year

#Daniel and Andrews
First_names = []
Last_names = []
Day = []
Month = []
Year = []
Repeat = 4
while Repeat == 4 :
    Initial_list = input("""Enter data as shown First name,Last name,DD,MM,YYYY, once done entering type "Done": """).split(",")
    Done = ("Done")
    for i in range(0, len(Initial_list)):
        Initial_list = [x.strip() for x in Initial_list]
    if Initial_list[0] == Done:
        Repeat = 0
    else:
        First_names.append(Initial_list[0])
        Last_names.append(Initial_list[1])
        Day.append(Initial_list[2])
        Month.append(Initial_list[3])
        Year.append(Initial_list[4])
Add = 0
Repeat = len(Year)/2
for i in range(0,int(Repeat)):
    print("--------------------------------------------------")
    print((First_names[0+Add] + " " + Last_names[0+Add]).ljust(25," ") + (Day[0 + Add] + "/" + Month[0 + Add] + "/" + Year[0 + Add]).rjust(25, " "))
    print((First_names[1+Add] + " " + Last_names[1+Add]).ljust(25," ") + (Day[1 + Add] + "/" + Month[1 + Add] + "/" + Year[1 + Add]).rjust(25, " "))
    Add += 2
if len(Year) % 2 != 0:
    print((First_names[len(Year)-1] + " " + Last_names[len(Year)-1]).ljust(25," ") + (Day[len(Year)-1] + "/" + Month[len(Year)-1] + "/" + Year[len(Year)-1]).rjust(25, " "))

