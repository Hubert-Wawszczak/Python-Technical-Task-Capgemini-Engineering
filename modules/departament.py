from dataclasses import dataclass, field
from typing import List

from modules.employer import Employer


@dataclass
class Department:
    id: int = 0
    departments_names = []

    def __init__(self, name):
        Department.id = Department.id + 1
        self.id_department = self.id
        self.name = name
        self.departments_names.append(self.name)
        self.users = []

    @classmethod
    def display_departments(cls):
        if cls.departments_names is None:
            print("No existing departments")
        else:
            for name in cls.departments_names:
                print(f"name of department {name}")

    def display_employers_in_department(self):
        if self.users is None:
            print(f"No existing employers in {self.name}")
        else:
            for name in self.users:
                print(name)

    def __str__(self):
        return f" id: {str(self.id_department)} department name: {self.name}"
