import openpyxl
from datetime import datetime

def create_favorite_people_file():
    current_year = datetime.now().year
    people_data = []
    filename = "favorite_people.xlsx"

    print("--- Enter details for your 3 favorite people ---")

    for i in range(1, 4):
        print(f"\nPerson #{i}:")
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        
        try:
            birth_year = int(input("Birth Year: "))
            age = current_year - birth_year
            person_id = i
            people_data.append([person_id, first_name, last_name, birth_year, age])
        except ValueError:
            print("Invalid input for birth year. Please restart the program and enter a number.")
            return

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Favorite People"

    headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    sheet.append(headers)

    for person in people_data:
        sheet.append(person)

    workbook.save(filename)
    print(f"\nSuccessfully saved to {filename}!")

    print("\n--- Saved Records ---")
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Birth Year':<12} {'Age':<5}")
    print("-" * 55)
    
    for row in people_data:
        p_id, f_name, l_name, b_year, age = row
        print(f"{p_id:<5} {f_name:<15} {l_name:<15} {b_year:<12} {age:<5}")

if __name__ == "__main__":
    create_favorite_people_file()
