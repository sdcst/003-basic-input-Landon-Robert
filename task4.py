#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

radius = input("\n\nWhat is the radius of the cone?")
height = input("\n\nWhat is the height of the cone?")
r = int(radius)
h = int(height)

SA = 3.14159265*r*(r+(h**2 + r**2)**0.5)

print(f"your answer is {SA}")