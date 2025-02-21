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

#Calculating the wage of the employee and partimers
def calculate_wage():
    attendance = Check_Attendance()
    match attendance:
        case 1:
            wage = 20 * 8
            print(f"Wage of the Employee is: {wage}")
        case 2:
            wage = 20 * 4
            print(f"Wage of the Partime Employee is: {wage}")
        case _:
            print("Wage of the Employee is: 0")

calculate_wage()