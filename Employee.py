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
    month_days=20
    pay_per_hour=20
    match attendance:
        case 1:
            hours = 8
            wage = hours * pay_per_hour
            monthly_wage = wage * month_days
            print(f"Wage of the Employee for the day is: {wage} and his/her's monthly wage is: {monthly_wage}")
        case 2:
            hours = 4
            wage = hours * pay_per_hour
            monthly_wage = wage * month_days
            print(f"Wage of the Partime Employee for the day is: {wage} and his/her's monthly wage is: {monthly_wage}")
        case _:
            print("Wage of the Employee is: 0")

calculate_wage()