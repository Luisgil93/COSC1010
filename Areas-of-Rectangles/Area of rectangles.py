#
# Name Luis Gil
# Date 09/15/2024
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables
lenghtA = 0 # Length of Rectangle A
widthA =0 # Width of Rectangle A
areaA =0 # Area of Rectanghle A

lengthB = 0 # Length of Rectangle B
widthB = 0 # Width of Rectangle B
areaB = 0 # Area of Rectangle B
# Get length A
lengthA=int(input('Enter the length of rectangle A: '))
# Get width A
widthA=int(input('Enter the width of rectangle A: '))
# Get length B
lengthB=int(input('Enter the length of rectangle B: '))
# Get width B
widthB=int(input('Enter the width for rectangle B: '))
# Calculate area A
areaA=lengthA*widthA
# Calculate area B
areaB=lengthB*widthB
# Print area comparison using if-elif-else statements
if areaA > areaB:
  print('rectangle A has the greater area.')
elif areaB > areaA:
  print('rectangle B has the greater area.')
else:
  print('Both have the same area.')