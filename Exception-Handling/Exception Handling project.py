#
# Name, Luis Gil
# Date, 10/27/2024
# Exception Handling Programming Project
# COSC 2409 DNT

# Main Function
def main():
    try:
        # Open the files.
        numbersFile = open("numbers.txt", "r" )
        total = 0
        numberOfLines = 0
        # Read the first line.
        line = numbersFile.readline()
        # Loop each line
        while line !="":
            numberOfLines += 1
            total += int( line )
            line = numbersFile.readline()
        # Calculate the average 
        average = total / numberOfLines
    except IOError as error:
        print( "An IOError occured:", error )
    except ValueError as error:
        print(" A ValueError occured:", error )
    else:
        print( "The average is", average )
    finally:
        print( "End of program ")

# Call out the main function.
    main()
