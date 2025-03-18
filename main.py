# Main file
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name, department):
        self.__employee_id = employee_id  
        self.__name = name
        self.__department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("--- Employee Details ---")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")

class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, department, basic_salary, bonus):
        super().__init__(employee_id, name, department)
        self.__basic_salary = basic_salary
        self.__bonus = bonus

    def calculate_salary(self):
        return self.__basic_salary + self.__bonus

    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self.__basic_salary:.2f}")
        print(f"Bonus: ${self.__bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class ContractEmployee(Employee):
    def __init__(self, employee_id, name, department, hourly_rate, hours_worked):
        super().__init__(employee_id, name, department)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked

    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self.__hourly_rate:.2f}")
        print(f"Hours Worked: {self.__hours_worked}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class Intern(Employee):
    def __init__(self, employee_id, name, department, stipend):
        super().__init__(employee_id, name, department)
        self.__stipend = stipend

    def calculate_salary(self):
        return self.__stipend

    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self.__stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

permanent_emp = PermanentEmployee("P123", "Adhithyan", "IT", 600000, 50000)
contract_emp = ContractEmployee("C456", "Jeeva", "HR", 90, 160)
intern_emp = Intern("I789", "Smith", "Finance", 2500)

permanent_emp.display_details()
contract_emp.display_details()
intern_emp.display_details()

