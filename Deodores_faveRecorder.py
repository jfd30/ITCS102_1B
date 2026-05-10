import openpyxl
from datetime import datetime

def create_favorite_people_file():
    # 1. Initialize variables
    current_year = datetime.now().year
    people_data = []
    filename = "favorite_people.xlsx"

    print("--- Enter details for your 3 favorite people ---")

    # 2. Accept user input for 3 people
    for i in range(1, 4):
        print(f"\nPerson #{i}:")
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        
        try:
            birth_year = int(input("Birth Year (e.g., 1995): "))
            # 3. Automatically compute age and assign ID
            age = current_year - birth_year
            person_id = i
            
            # Store data in a list to process later
            people_data.append([person_id, first_name, last_name, birth_year, age])
        except ValueError:
            print("Invalid input for birth year. Please restart the program and enter a number.")
            return

    # 4. Create and write data into an Excel file
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Favorite People"

    # Define Column Headers
    headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    sheet.append(headers)

    # 5. Store all user input in the Excel file
    for person in people_data:
        sheet.append(person)

    # Save the file
    workbook.save(filename)
    print(f"\nSuccessfully saved to {filename}!")

    # 6. Display all saved records in the console
    print("\n--- Saved Records ---")
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Birth Year':<12} {'Age':<5}")
    print("-" * 55)
    
    for row in people_data:
        p_id, f_name, l_name, b_year, age = row
        print(f"{p_id:<5} {f_name:<15} {l_name:<15} {b_year:<12} {age:<5}")

if __name__ == "__main__":
    create_favorite_people_file()
