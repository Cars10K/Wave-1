import math

Radius = float(input("Please enter a radius for a cylinder: "))
Height = float(input("Please enter the height of the cylinder: "))

Volume = math.pi * (Radius * Radius) * Height

print("The volume of this cylinder is {0:0.01f} units cubed.".format(Volume))