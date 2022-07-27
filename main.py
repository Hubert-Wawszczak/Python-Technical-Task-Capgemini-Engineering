
from  modules.employer import Employer
from modules.company import Company

if __name__ == "__main__":
    obj = Company()
    obj.create_employer()
    obj.create_department()
    obj.add_employer_to_department()