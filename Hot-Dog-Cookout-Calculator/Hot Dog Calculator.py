#
# Name Luis Gil
# Date 09/15/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.
#  Constant Variables
NUMBER_OF_HOTDOGS_PER_PACKAGE= 10
NUMBER_OF_BUNS_PER_PACKAGE= 8
# this program Calaculates The number of hotdogs needed for a cookout.
#Number of people Attending the cookout.
number_of_people= int(input('Enter the number of people:'))
#Number of Hot Dogs per person.
number_of_hotdogs_per_person= int(input('Enter number of hotdogs:'))
#Total number of Hotdogs needed.
total_number_of_hotdogs= number_of_people * number_of_hotdogs_per_person

number_of_hotdog_packages_needed = total_number_of_hotdogs // NUMBER_OF_HOTDOGS_PER_PACKAGE
number_of_hotdog_buns_needed = total_number_of_hotdogs // NUMBER_OF_BUNS_PER_PACKAGE
number_of_hotdogs_left_over = total_number_of_hotdogs % NUMBER_OF_HOTDOGS_PER_PACKAGE
number_of_hotdog_buns_left_over = total_number_of_hotdogs % NUMBER_OF_BUNS_PER_PACKAGE
#Text For the user.
print("Minimum number of packages of hot dogs required =", number_of_hotdog_packages_needed)
print("Minimum number of packages of hotdog buns required =", number_of_hotdog_buns_needed)
# Amount of hot dogs left over.
print("Number of hotdogs left over=", number_of_hotdogs_left_over)
# Amount of hot dog buns left over.
print("Number of hotdog buns left over =", number_of_hotdog_buns_left_over)