from modules.employer import *
from modules.departament import *
import pickle


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
        self.display_unattached_workers()
        id_to_rm = input("Enter id of employer which you want delete")
        emp_to_remove = self.find_employer_by_id(id_to_rm)
        if not emp_to_remove:
            print("Wrong id")
            return False
        for emp in self.employers:
            if emp == emp_to_remove:
                self.employers.remove(emp_to_remove)

        for emp in self.employers:
            if emp.id_employer >= int(id_to_rm):
                emp.id_employer = emp.id_employer - 1
        emp.id = emp.id - 1

    def remove_department(self):
        Department.display_departments()
        id_to_rm = self.find_department_id_by_name(input("Enter name of department to remove"))
        if not id_to_rm:
            print("Wrong id")
            return False
        for dep in self.departments:
            if dep.id_department == int(id_to_rm):
                self.employers.remove(dep)

        for dep in self.departments:
            if dep.id_department >= int(id_to_rm):
                dep.id_department = dep.id_department - 1
        dep.id = dep.id - 1

    def apply_bonus_to_employer(self):
        self.display_unattached_workers()
        id_of_employer = input("Enter id of employer which you want give bonus")
        emp = self.find_employer_by_id(id_of_employer)
        emp.apply_bonus(input("Enter bonus value"))

    def apply_bonus_for_all_from_department(self):
        Department.display_departments()
        for dep in self.departments:
            dep.display_employers_in_department()

        for dep in self.departments:
            if dep.id_department == int(self.find_department_id_by_name(input("Enter department name"))):
                bonus = input(f"Give bonus for all from department {dep}")
                for emp in dep.users:
                    emp.apply_bonus(bonus)
                break

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
            if dep.id_department == int(departament_id):
                return dep
            else:
                print("Given department id doesn't exist")
                return False

    def find_employer_by_id(self, employer_id):
        for emp in self.employers:
            if emp.id_employer == int(employer_id):
                return emp

        print("Given employer id doesn't exist")
        return False

    def find_department_id_by_name(self, name):
        if not self.departments:
            print("None added departments")
            return False
        for dep in self.departments:
            if dep.name == name:
                print(dep)
                return dep.id_department
        print("Given name doesn't exist")
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
            self.find_department_id_by_name(input("Enter name of existing departament"))
            departament_id = input("Enter id of existing departament")

            dep = self.find_department_by_id(departament_id)
            emp = self.find_employer_by_id(employer_id)

            dep.users.append(emp)

    def save_employer_to_file(self, path):
        with open(path, "wb+") as file:
            for emp in self.employers:
                file.write(str(emp))
        file.close()
