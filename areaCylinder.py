#Find the surface area of a cylinder
import math
height = float(input("Enter the heigh in cm of the cylinder: "))
radius = float(input("Enter the radius in cm of the cylinder: "))
surfacearea = 2*(math.pi*radius*radius) + (2*math.pi*radius)*height
print("The surface area of the cylinder is: ", surfacearea,"cm") 
