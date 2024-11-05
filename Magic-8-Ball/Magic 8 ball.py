#
# Name luis
# Date
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
import random

def main():
    infile = open('8_ball_responses.txt', 'r')
    response_list = infile.readlines()
    for index in range(len(response_list)):
        response_list[index] = response_list[index].rstrip('\n')
    again = 'y'
    while again == 'y' or again == 'Y':
        qst =input('ask your question and get answer: ')
        print(response_list[random.randint(0, len(response_list) -1)])
        print("ask more question?")
        again = input('[y/n] to continue: ')
main()
