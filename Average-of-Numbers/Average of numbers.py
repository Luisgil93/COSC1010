#
# Name luis gil
# Date 10/21/2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
 
def main():
    try:
        numbersFile = open( 'numbers.txt', 'r' )
    except Exception as errorGenerated:
        print("File not found:", errorGenerated )
    else:
        total = 0
        numberOfLines = 0
        line= numbersFile.readline()

    while line != "":
        numberOfLines += 1
        total += int( line )
        line = numbersFile.readline()

        average = total / numberOfLines

        print( "The average is",average)

        main()
