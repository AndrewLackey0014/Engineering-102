# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab4_Act2_Prog1
# Date:		16/9/2019 day month year
Ticket_lost = False
End = 1
while End == 1:
    User_hours = input("""Enter how many hours and minutes separated by a ":" you were parked and if you lost the ticket enter a "-"(Ex. -4:0): """).split(":")
    for i in range(0, len(User_hours)):
        User_hours = [x.strip() for x in User_hours]  # removes spaces
    def Maybe_Float(User_hours):
        try:
            return int(User_hours)
        except (ValueError):
            User_hours = [s for s in User_hours if s.isdigit()]
    New_hours = [Maybe_Float(i) for i in User_hours] #creates a None value where a string is (using the def statement)
    New_hours = list(filter(None.__ne__,New_hours)) #gets rid of None value
    if New_hours[0] < 1:
        New_hours[0] = abs(New_hours[0])
        Ticket_lost = True
    if len(New_hours) == 1:
        print("Please enter in valid format")
    elif New_hours[1] > 60:
        print("stop resisting")
    elif len(New_hours) >= 3:
        print("Please enter a valid time")
    else:
        if New_hours[1] == 0:
            del New_hours[1]
            Round = New_hours[0]
            End = 2
        elif len(New_hours) == 2:
            del New_hours[1]
            Round = New_hours[0] + 1
            End = 2
        else:
            Round = New_hours[0]
            End = 2
if 0 < Round <= 2:
    Total = 4
elif 2 < Round <= 4:
    Total = 7
elif 4 < Round < 24:
    Total = Round + 3
elif Round > 24:
    Number_days = Round // 24
    Remainder = Round % 24
    if 0 < Remainder <= 2:
        Day_charge = 4
    elif 2 < Remainder <= 4:
        Day_charge = 7
    elif 4 < Remainder < 24:
        Day_charge = Remainder + 3
        if Day_charge > 24:
            Day_charge = 24
    Total = (Number_days * 24)+Day_charge
if Ticket_lost == True:
    Total = Total + 36
print("You were parked for",Round,"hours, pay $"+str(Total))
