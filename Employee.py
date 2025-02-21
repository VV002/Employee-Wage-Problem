import os

#Getting the width of the terminal to center the title
width = os.get_terminal_size().columns

#Printing the title
print("-------------------------------WELCOME TO EMPLOYEE WAGE COMPUTATION-------------------------------".center(width))