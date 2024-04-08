#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

print ("\nInput variables for an equation in ax + b = c format")
A = input ("\n\nVariable for a: ")
B = input ("\n\nVariable for b: ")
C = input ("\n\nVariable for c: ")
a = int(A)
b = int(B)
c = int(C)
x = (c-b)/a

print(f"Your answer is {x}")
