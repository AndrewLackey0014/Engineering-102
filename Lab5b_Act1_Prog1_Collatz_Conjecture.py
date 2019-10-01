# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Andrew Lackey
# Section:		533
# Assignment:	Lab5b_Act1_Prog1 (e.g. Lab 1b-2)
# Date:		24/9/2019 day month year
print("\nThis program evaluates The Collatz conjecture which takes any whole number (n)"
      "\ngreater than 0 and if n is odd does the expression 3n-1 and if n"
      "\nis even does the expression n/2 until n reaches 1.")
End = 1
# Loop lets the user select a number for n
while End == 1:
    try:
        End += 1
        N = int(input("\nn: "))
        if N <= 0:
            print("\nPlease input an integer greater than 0")
            End -= 1
    except ValueError:
        print("\nPlease enter a valid integer")
        End -= 1
Sequence = [N]
Iterations = 0
# Loop checks to make sure it agrees with the Collatz conjecture
while N != 1:
    Odd = N % 2
    if Odd > 0:
        N = (3*N + 1)
    else:
        N = N/2
    Sequence.append(int(N))
    Iterations += 1
# Three statements will print out the iterations sequence and ending digit depending on
# How many times it looped to help with grammar
if Iterations == 1:
    print("\nThe program took %g iteration to evaluate" % Iterations,
          "\nThe sequence of numbers is \n%s" % Sequence,
          "\nThe sequence ended at %g" % int(N))
elif Iterations == 0:
    print("\nThe program didn't need any iterations to evaluate",
          "\nThe sequence of numbers is \n%s" % Sequence,
          "\nThe sequence ended at %g" % int(N))
else:
    print("\nThe program took %g iterations to evaluate" % Iterations,
          "\nThe sequence of numbers is \n%s" % Sequence,
          "\nThe sequence ended at %g" % int(N))
