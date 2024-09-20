#
# Name Luis Gil
# Date 09/20/2024
# Bug Collector Programming Project
# COSC 2409 DNT
#
# Initialize variables for bugs and total number of bugs collected.
total = 0
bugs = 0
day = 0
# Get number of bugs collected each day using a for loop.
for day in range (1, 8):
    print('Enter the bugs collected on day', day)
    # Input the number of bugs
    bugs = int(input ())
    #Add bugs to total
    total = total + bugs
# Display the total number of bugs collected.
print('You collected a total of', total, 'bugs.')