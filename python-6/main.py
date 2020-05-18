class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Employee:
    def employ(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.carga_horaria = 8
    def calc_bonus(self):
        return 0
    def get_hours(self):
        return self.carga_horaria

class Manager(Employee):
    def __init__(self, code, name, salary):
        self.employ(code, name, salary)
        self.__department = Department('managers', 1)
    def calc_bonus(self):
        return self.salary * 0.15
    def get_departament(self):
        return self.__department.name
    def set_department(self,department,code):
        self.__department = Department(department,code)

class Seller(Employee):
    def __init__(self, code, name, salary):
        self.employ(code, name, salary)
        self.__department=Department('sellers', 2)
        self.__sales=0
    def put_sales(self,new_sales):
        self.__sales = new_sales+self.__sales
    def get_sales(self):
        return self.__sales
    def calc_bonus(self):
        return self.get_sales()*0.15
    def get_departament(self):
        return self.__department.name
    def set_department(self,department,code):
        self.__departament = Department(department,code)