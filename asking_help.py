import math

radius = 3
area = math.pi * radius * radius

print(f'The area of the circle is {area}')
# return the area with max three decimal places

# Googling
# Too general ----- sweet spot ----- too specific
# Too general:   "Python format numbers"
# Sweet spot:    "Python how to format numbers to three decimal places in f-strings"
# Too specific:  "Python how to get the area of a circle to three decimal places"

print(f'The area of the circle is {area:.3f}')

