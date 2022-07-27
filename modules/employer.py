from dataclasses import dataclass


@dataclass()
class Employer:
    id: int = 0

    def __init__(self, first_name: str, last_name: str, age: int, job: str, salary: float, bonus: float):
        Employer.id = Employer.id + 1
        self.id_employer = self.id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus
        self.total_salary = self.salary + self.bonus

    def apply_bonus(self, bonus):
        self.bonus = bonus
        self.total_salary = self.salary + self.bonus

    def __str__(self):
        return f"id: {str(self.id_employer)} first_name: {self.first_name} last name: {self.last_name} age: {str(self.age)} job: {self.job} salary: {str(self.salary)} bonus: {str(self.bonus)} total salary: {str(self.total_salary)}"


