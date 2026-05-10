import openpyxl
from datetime import datetime
import os

def calculate_age(birth_year):
    """Computes age based on the current year."""
    current_year = datetime.now().year
    return current_year - birth_year

def main():
    filename = "favorite_people.xlsx"
    people_data = []

    print("--- Favorite People Recorder ---")
    
    # 1. Ask user for information for THREE people
    for i in range(1, 4):
        print(f"\nEnter details for Person #{i}:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        
        while True:
            try:
                birth_year = int(input("Birth Year (YYYY): "))
                break
            except ValueError:
                print("Invalid input. Please enter a numerical year.")

        # 2 & 3. Compute age and assign ID
        age = calculate_age(birth_year)
        person_id = i
        
        # Store in a temporary list
        people_data.append([person_id, first_name, last_name, birth_year, age])

    # 4 & 5. Create Excel file and define columns
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Favorite People"
    
    headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    sheet.append(headers)

    # 6. Store all input in the Excel file
    for person in people_data:
        sheet.append(person)

    workbook.save(filename)
    print(f"\nSuccess! Records have been saved to {filename}.")

    # 7. Display all saved records in the console
    print("\n--- Saved Records Summary ---")
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Birth Year':<12} {'Age':<5}")
    print("-" * 55)
    
    for row in people_data:
        p_id, f_name, l_name, b_year, p_age = row
        print(f"{p_id:<5} {f_name:<15} {l_name:<15} {b_year:<12} {p_age:<5}")

if __name__ == "__main__":
    main()
