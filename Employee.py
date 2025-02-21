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
    return attendace

#Calculating the wage of the employee
def calculate_wage():
    attendance = Check_Attendance()
    if attendance == 1:
        wage = 20 * 8
        print(f"Wage of the Employee is: {wage}")
    else:
        print("Since Employee is Absent so no wage is given")

calculate_wage()