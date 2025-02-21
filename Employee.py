import os
import random

#Getting the width of the terminal to center the title
width = os.get_terminal_size().columns

#Printing the titles
print("-------------------------------WELCOME TO EMPLOYEE WAGE COMPUTATION-------------------------------".center(width))

#Function to check the attendance of the employee and partimers
def Check_Attendance():
    attendace = random.randint(0,2)
    if attendace == 0:
        print("Employee is Absent")
    elif attendace == 1:
        print("Regular Employee is Present")
    else:
        print("Partime Employee is Present")

#Function call to check the attendance
Check_Attendance()
