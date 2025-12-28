import os
import json

os.system('cls')
print("STUDENT INFORMATION SYSTEM")

student_record = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - Add Student Record")
    print("B - Print All Student Record")
    print("C - Search Student Record")
    print("D - Delete Student Record")
    print("E - Edit Student Record")
    print("F - Export Student Record")
    print("G - Import Student Record")
    print("X - Exit System")

    choice = input("SELECT FROM THE OPTIONS").lower()
    os.system('cls')
    if choice == 'a':
        print("\nADDING STUDENT RECORD")

        id_no = input("Please Input Student ID Number: ")
        first_name = input("Please Input Student First Name: ").upper()
        second_name = input("Please Input Student Second Name: ").upper()
        age = eval(input("Input Student Age: "))
        course = input("Input Student Course: ").upper()
        section = input("Input Student Section: ").upper()

        student_record [id_no] = [first_name, second_name, age, course, section]
        print("DATA SAVED SUCCESSFULLY")

        continue

    elif choice == 'b':
        os.system('cls')
        print("\nPRINTING STUDENT RECORD")
        for xy, hehe in student_record.items():
            print(f"CODE - {xy}, INFORMATION - {hehe}")
            
        continue

    elif choice == 'c':
        os.system('cls')
        print("\nSEARCH STUDENT RECORD")
        search_id = input("Enter student ID to search: ").lower()
        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(f"RECORD FOUND for ID {search_id}")
                for gela in student_record[search_id]:
                    print(f" - - - {gela}")
            else:
                print("Sorry, NO RECORD FOUND")
            break
        continue


    elif choice == 'd':
        os.system('cls')
        print("\nDELETE STUDENT RECORD")
        search_id = input("Enter student ID to search: ").lower()
        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(f"RECORD FOUND for ID {search_id}")
                for gela in student_record[search_id]:
                    print(f" - - - {gela}")
                student_record.pop(search_id)
                print("RECORD DELETED")
            else:
                print("Sorry, NO RECORD FOUND")
            break
        continue

    elif choice == 'e':
        os.system('cls')
        print("\nEDIT STUDENT RECORD")
        search_id = input("Enter student ID to search: ").lower()
        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(f"RECORD FOUND for ID {search_id}")
                for gela in student_record[search_id]:
                    print(f" - - - {gela}")

                first_name = input("Please Input Student First Name: ").upper()
                second_name = input("Please Input Student Second Name: ").upper()
                age = eval(input("Input Student Age: "))
                course = input("Input Student Course: ").upper()
                section = input("Input Student Section: ").upper()

                student_record[search_id][0] = first_name
                student_record[search_id][1] = second_name
                student_record[search_id][2] = age
                student_record[search_id][3] = course
                student_record[search_id][4] = section
        
                print("DATA UPDATED")

            else:
                print("Sorry, NO RECORD FOUND")
            break
        continue
        

    elif choice == 'f':
        os.system('cls')
        print("EXPORT STUDENT DATA")
        with open('student_records.json', 'w') as new_file:
            json.dump(student_record, new_file, indent=4 )
            print("\n\nDATA EXPORTED TO JSON") 
        continue

    elif choice == 'g':
        os.system('cls')
        print("IMPORT STUDENT DATA")
        with open('student_records.json', 'r') as new_file:
            imported_files = json.load(new_file)

        student_record = imported_files
        print("\n\nDATA IMPORTED TO JSON") 
        continue

    elif choice == 'x':
        pass 
        break
    
    else: 

        print("INVALID CHOICE, REENTER YOUR CHOICE")
