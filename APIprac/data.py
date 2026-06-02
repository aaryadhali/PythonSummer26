import json

class EmployeeRegistry:
    def __init__(self):
       # Outer dictionary to store all employees
       self.employees = {}

    def add_employee(self, emp_id, name, email, dob): #, dob, salary):
        # inner dict uses emp_id as a key
        self.employees[emp_id] = {
            "name": name, 
            "email": email,
            "date_of_birth": dob   
        }
        # key:
        #self.emp_id = emp_id 
        # vlaues:
    
        # self.dob = dob
        # self.salary = salary

    def get_employee(self, emp_id):
        return self.employees.get(emp_id, "employee not found")
    
    def print_dict(self, dict):
        print(json.dumps(dict, indent = 4))
    


registry = EmployeeRegistry()

registry.add_employee(1, "Aarya", "aaryasspot@gmail.com", "08-12-05")
registry.add_employee(2, "Jaspal", "jasdhalidocs@gmail.com", "03-02-70")

registry.print_dict(registry.employees)
