from abc import ABC, abstractmethod

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')


class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

"""
The DisgruntledEmployee class doesn’t derive from Employee, but it exposes 
the same interface required by the PayrollSystem. 
The PayrollSystem.calculate_payroll() requires a list of objects that 
implement the following interface:

An id property or attribute that returns the employee’s id
A name property or attribute that represents the employee’s name
A .calculate_payroll() method that doesn’t take any parameters and returns 
the payroll amount to process
All these requirements are met by the DisgruntledEmployee class, so the 
PayrollSystem can still calculate its payroll.
"""
class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 1000000


if __name__ == "__main__":

    salary_employee = SalaryEmployee(1, 'John Smith', 1500)
    hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
    commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
    disgruntled_employee = DisgruntledEmployee(20000, 'Anonymous')
    payroll_system = PayrollSystem()
    payroll_system.calculate_payroll([
        salary_employee,
        hourly_employee,
        commission_employee,
        disgruntled_employee
    ])
