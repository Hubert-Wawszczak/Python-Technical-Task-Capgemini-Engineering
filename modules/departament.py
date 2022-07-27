from dataclasses import dataclass, field
from typing import List

from modules.employer import Employer


@dataclass
class Department:
    id: int = 0
    departments_names = []

    def __init__(self, name):
        self.id = self.id + 1
        self.id_department = self.id + 1
        self.name = name
        self.departments_names.append(self.name)
        self.users = []

    def display_departments(self):
        if self.departments_names is None:
            print("No existing departments")
        else:
            for name in self.departments_names:
                print(f"id: {str(name.id_department)} name of department {name.name}")

    def display_employers_in_department(self):
        if self.users is None:
            print(f"No existing employers in {self.name}")
        else:
            for name in self.users:
                print(name)
