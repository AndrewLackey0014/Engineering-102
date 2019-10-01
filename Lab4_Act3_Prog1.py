# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Andrew Lackey
# 	 		Duane Craig
# 	 		Kevin Swedlund
#			Daniel Sanchez
# Section:		533
# Assignment:	Lab4_Act3_Prog1
# Date:		17/9/2019 day month year

#Part A
print("\nPart A and B")
End = 1
while End == 1:
    A = input("""\nPlease input "True" or "False" or "T" or "F" or "t" or "f" for A: """).strip()
    if A == "True" or A == "T" or A == "t":
        A = bool(1)
        End +=1
    elif A == "False" or A == "F" or A == "f":
        A = bool(0)
        End += 1
    else:
        print("\nPlease input a valid statement")
End = 1
while End == 1:
    B = input("""\nPlease input "True" or "False" or "T" or "F" or "t" or "f" for B: """).strip()
    if B == "True" or B == "T" or B == "t":
        B = bool(1)
        End +=1
    elif B == "False" or B == "F" or B == "f":
        B = bool(0)
        End += 1
    else:
        print("\nPlease input a valid statement")
End = 1
while End == 1:
    C = input("""\nPlease input "True" or "False" or "T" or "F" or "t" or "f" for C: """).strip()
    if C == "True" or C == "T" or C == "t":
        C = bool(1)
        End +=1
    elif C == "False" or C == "F" or C == "f":
        C = bool(0)
        End += 1
    else:
        print("\nPlease input a valid statement")
print(bool(A and B and C)) #Part B
print(bool(A or B or C)) #Part B
print("\nPart C")
#Part C-1
A = bool(0) #False
B = bool(1) #True
print(not(A==B))
#Part C-2
A = bool(0)
B = bool(0)
C = bool(0)
#COPY HERE
#part C-3
End = 1
while End == 1:
    A = input("""\nPlease input "True" or "False" or "T" or "F" or "t" or "f" for A: """).strip()
    if A == "True" or A == "T" or A == "t":
        A = bool(1)
        End +=1
    elif A == "False" or A == "F" or A == "f":
        A = bool(0)
        End += 1
    else:
        print("\nPlease input a valid statement")
End = 1
while End == 1:
    B = input("""\nPlease input "True" or "False" or "T" or "F" or "t" or "f" for B: """).strip()
    if B == "True" or B == "T" or B == "t":
        B = bool(1)
        End +=1
    elif B == "False" or B == "F" or B == "f":
        B = bool(0)
        End += 1
    else:
        print("\nPlease input a valid statement")
End = 1
while End == 1:
    C = input("""\nPlease input "True" or "False" or "T" or "F" or "t" or "f" for C: """).strip()
    if C == "True" or C == "T" or C == "t":
        C = bool(1)
        End +=1
    elif C == "False" or C == "F" or C == "f":
        C = bool(0)
        End += 1
    else:
        print("\nPlease input a valid statement")
print((not (A and not B) or (not C and B)) and (not B) or (not A and B and not C) or (A and not B))
print((not ((B or not C) and (not A or not C))) or (not (C or not (B and C))) or (A and not C) and (not A or (A and B and C) or (A and ((B and not C) or (not B)))))
# symplified
print(not B or (not C and not A))
print(A or ((not C and A) or C) and not B)
