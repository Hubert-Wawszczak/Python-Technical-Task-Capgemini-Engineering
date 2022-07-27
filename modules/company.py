from modules.employer import *
from modules.departament import *


class Company:
    def __init__(self):
        self.employers = []
        self.departments = []

    def create_employer(self):
        self.employers.append(Employer(input('Enter employer name:'),
                                       input('Enter employer last name:'),
                                       input('Enter employer age:'),
                                       input('Enter employer job:'),
                                       input('Enter employer salary:'),
                                       input('Enter employer bonus:')
                                       ))
        print("Successfully added new employer")

    def remove_employer(self):
        

    def create_department(self):
        self.departments.append(Department(input("Enter department name")))
        print("Successfully added new department")

    def display_unattached_workers(self):
        if not self.employers:
            print("None employers exist")
        else:
            for emp in self.employers:
                print(f"id: {emp.id_employer} first name: {emp.first_name} last name {emp.last_name}")

    def find_department_by_id(self, departament_id):
        for dep in self.departments:
            if dep.id_department == departament_id:
                return dep
            else:
                print("Given department id doesn't exist")
                return False

    def find_employer_by_id(self, employer_id):
        for emp in self.employers:
            if emp.id_employer == employer_id:
                return emp
            else:
                print("Given employer id doesn't exist")
                return False

    def add_employer_to_department(self):
        if not self.departments:
            print("None department exist")
        elif not self.employers:
            print("None employers exist")
        else:

            self.display_unattached_workers()
            employer_id = input("Enter id of existing employer")

            Department.display_departments()
            departament_id = input("Enter id of existing departament")

            dep = self.find_department_by_id(departament_id)
            emp = self.find_employer_by_id(employer_id)

            dep.users.append(emp)
