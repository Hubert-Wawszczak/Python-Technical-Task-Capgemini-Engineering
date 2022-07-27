from modules.employer import Employer
from modules.company import Company

if __name__ == "__main__":
    obj = Company()
    x = 1
    while x != 0:
        print("Select option")
        print(" 1 - Add new employer")
        print(" 2 - Add department employer")
        print(" 3 - Add employer to department")
        print(" 4 - Remove employer")
        print(" 5 - Remove  department")
        print(" 6 - Apply bonus to employer")
        print(" 7 - Apply bonus to employers from department ")
        print(" 8 - Save all employers to file ")
        x = input("Give number to select operation")
        x = int(x)
        if x == 1:
            obj.create_employer()
        elif x == 2:
            obj.create_department()
        elif x == 3:
            obj.add_employer_to_department()
        elif x == 4:
            obj.remove_employer()
        elif x == 5:
            obj.remove_department()
        elif x == 6:
            obj.apply_bonus_to_employer()
        elif x == 7:
            obj.apply_bonus_for_all_from_department()
        elif x == 8:
            obj.save_employer_to_file(input("Give path to file"))
  
