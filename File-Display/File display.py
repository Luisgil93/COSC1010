#
# Name Luis Gil
# Date, 10/20/2024
# File Display Programming Project
# COSC 2409 DNT

# Open the file.
myfile = open('numbers.txt', 'r')

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

