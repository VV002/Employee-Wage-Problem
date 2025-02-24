import os
import random

class Employee_wage:
    """
        Description:
            This class is used to calculate the wage of the employee and partimers.
            It has a static method to check the attendance of the employee and partimers.
            It has a method to calculate the wage of the employee and partimers.
            It has a method to print the wage of the employee and partimers.
        Parameters: 
            None
        Return:
            None
    """
    max_hours=100
    max_days=20

    def __init__(self):
        """
            Description:
                This constructor is used to intialize the instance variables.
            Parameters:
                None
            Return:
                None
        """
        self.emp_hours, self.emp_wage,self.emp_days = 0,0,0
        self.partime_days, self.partime_hours, self.partime_wage = 0,0,0
        self.absent_days = 0
        self.total_hours = 0
        self.total_days = 0

    def print_wage(self):
        """
            Description:
                This method is used to print the wage of the employee and partimers.
            Parameters:
                None
            Return:
                None
        """
        print(f"Total days worked: {self.total_days} and Total hours worked: {self.total_hours}")
        print(f"Employee worked for {self.emp_days} days and {self.emp_hours} hours and earned ${self.emp_wage}")
        print(f"Partimer worked for {self.partime_days} days and {self.partime_hours} hours and earned ${self.partime_wage}")
        print(f"Employees was absent for {self.absent_days} days")

    
    #Static method checks the attendance of the employee and partimers
    @staticmethod
    def Check_Attendance():
        return random.randint(0,2)

    def calculate_wage(self):
        """
            Description:
                This method is used to calculate the wage of the employee and partimers.
            Parameters:
                None
            Return:
                None
        """
        while self.total_hours < self.max_hours and self.total_days < self.max_days:
            if self.Check_Attendance()==1:
                hours = 8
                wage = hours * 20
                self.emp_wage+=wage
                self.emp_hours+=hours
                self.emp_days+=1
                self.total_days+=1
                self.total_hours+=hours

            elif self.Check_Attendance()==2:
                hours = 4
                wage = hours * 20
                self.partime_wage+=wage
                self.partime_hours+=hours
                self.partime_days+=1
                self.total_days+=1
                self.total_hours+=hours

            else:
                self.total_days+=1
                self.absent_days+=1
        self.print_wage()


def main():

    #Getting the width of the terminal to center the title
    width = os.get_terminal_size().columns

    #Printing the titles
    print("-------------------------------WELCOME TO EMPLOYEE WAGE COMPUTATION-------------------------------".center(width))
    wage = Employee_wage() #instance/object of the class
    wage.calculate_wage()   


if __name__ == "__main__":
    main()