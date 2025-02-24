import os
import random

#Getting the width of the terminal to center the title
width = os.get_terminal_size().columns

#Printing the titles
print("-------------------------------WELCOME TO EMPLOYEE WAGE COMPUTATION-------------------------------".center(width))

#Function to check the attendance of the employee and partimers
def Check_Attendance():
    return random.randint(0,2)

#Function to print the wage of the employee and partimers
def print_wage(eh,ed,ew,ph,pd,pw,ad,td,th):
    print(f"Total days worked: {td} and Total hours worked: {th}")
    print(f"Employee worked for {ed} days and {eh} hours and earned ${ew}")
    print(f"Partimer worked for {pd} days and {ph} hours and earned ${pw}")
    print(f"Employee was absent for {ad} days")

#Calculating the wage of the employee and partimers
def calculate_wage():
    emp_hours, emp_wage,emp_days = 0,0,0
    partime_days, partime_hours, partime_wage = 0,0,0
    absent_days = 0
    total_hours = 0
    total_days = 0
    max_hours=100
    max_days=20
    while total_hours < max_hours and total_days < max_days:
        attendance = Check_Attendance()
        if attendance==1:
            hours = 8
            wage = hours * 20
            emp_wage+=wage
            emp_hours+=hours
            emp_days+=1
            total_days+=1
            total_hours+=hours

        elif attendance==2:
            hours = 4
            wage = hours * 20
            partime_wage+=wage
            partime_hours+=hours
            partime_days+=1
            total_days+=1
            total_hours+=hours
            
        else:
            total_days+=1
            absent_days+=1
    print_wage(emp_hours,emp_days,emp_wage,partime_hours,partime_days,partime_wage,absent_days,total_days,total_hours)        

calculate_wage()