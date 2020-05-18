class Department:
    """ Represents the employee department.
    """
    def __init__(self, name, code):
        """ Class constructor.

        Arguments:
            name {string} -- employee department.
            code {int} -- department code.
        """
        self.name = name # Defines the department name. 
        self.code = code # Defines the department code.

class Employee:
    """ This class represents the employee's major class.
    """
    def register_employee(self, code, name, salary):
        """ This function register the employee in the company records
        Arguments:
            code {int} -- employee number
            name {string} -- employee name
            salary {float} -- employee salary
        """
        self.__code = code # Defines the employee's code.
        self.__name = name # Defines the employee's name.
        self.__salary = salary # Defines the employee's salary.
        self.__workload = 8 # Defines the employee's workload.
    
    def calc_bonus(self):
        return 0 # Returns the employee's bonus.
    
    def get_hours(self):
        return self.__workload # Returns the employee's workload.
    
    def get_salary(self):
        return self.__salary # Returns the employee's salary.

class Manager(Employee):
    """ Manager is an employee subclass, represents a manager of the company.
    """
    def __init__(self, code, name, salary):
        """ Class constructor.
        Arguments:
            code {int} -- The employee's code.
            name {string} -- The employee's name.
            salary {float} -- The employee's salary.
        """
        self.register_employee(code, name, salary)# Defines the employee's information.
        self.__department = Department('managers', 1) # Defines the employee's department.
    
    def calc_bonus(self):
        return self.get_salary()*0.15 # Returns the manager bonus.
    
    def get_departament(self):
        return self.__department.name # Returns the manager department name.
    
    def set_department(self,new_department,new_code):
        self.__department = Department(new_department,new_code) # Set department new name.


class Seller(Employee):
    """ Seller is an employee subclass, represents a seller of the company.
    """
    def __init__(self, code, name, salary):
        """ Class constructor.
        Arguments:
            code {int} -- The employee's code.
            name {string} -- The employee's name.
            salary {float} -- The employee's salary.
        """
        self.register_employee(code, name, salary) # Defines the employee's information.
        self.__department=Department('sellers', 2) # Defines the employee's department.
        self.__sales=0 # Defines the employee's sales number.
    
    def put_sales(self,new_sales):
        self.__sales = new_sales+self.__sales # Adjusts the sales number.
    
    def get_sales(self):
        return self.__sales # Gets the number of sales.
    
    def calc_bonus(self):
        return self.get_sales()*0.15 # Calculates the employer bonus.
    
    def get_departament(self):
        return self.__department.name # Get the employee's department name.
    
    def set_department(self,new_department,new_code):
        self.__departament = Department(new_department,new_code) # Adjusts the employee's department name. 