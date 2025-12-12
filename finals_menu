import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_screen():
    clear_screen()
    print("====================================")
    print("      WELCOME TO PYTHON MENU")
    print("====================================")

    name = input("Hello! What's your name? ")
    print(f"Nice to meet you, {name}!")

    while True:
        cont = input("Do you want to continue? (yes/no): ").strip().lower()

        if cont == "yes":
            return  # Go to main menu
        elif cont == "no":
            print("\nThank you for using the program!")
            exit()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


# ============================================
# MAIN MENU
# ============================================
def main_menu():
    while True:
        clear_screen()
        print("====================================")
        print("   PYTHON FUNDAMENTALS MAIN MENU")
        print("====================================")
        print("[1] Print Statements")
        print("[2] Variables")
        print("[3] Operators")
        print("[4] Conditionals")
        print("[5] Loops")
        print("[6] Lists")
        print("[7] Functions")
        print("[8] Run Your Own Python Code")
        print("[0] Exit Program")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            submenu_print()
        elif choice == "2":
            submenu_variables()
        elif choice == "3":
            submenu_operators()
        elif choice == "4":
            submenu_conditionals()
        elif choice == "5":
            submenu_loops()
        elif choice == "6":
            submenu_lists()
        elif choice == "7":
            submenu_functions()
        elif choice == "8":
            run_user_program()
        elif choice == "0":
            print("\nThank you for using the program!")
            break
        else:
            input("Invalid input. Press Enter to try again...")


# ============================================
# PRINT STATEMENTS SUBMENU
# ============================================
def submenu_print():
    while True:
        clear_screen()
        print("==== PRINT STATEMENTS MENU ====")
        print("[1] Simple Print Example")
        print("[2] Multiple Prints")
        print("[0] Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nExample: Simple Print Statement")
            print("Hello, World!")
            input("\nPress Enter to continue...")
        elif choice == "2":
            print("\nExample: Multiple Print Outputs")
            print("Python is fun!")
            print("This is a print statement example.")
            input("\nPress Enter to continue...")
        elif choice == "0":
            return
        else:
            input("Invalid choice. Press Enter to try again...")


# ============================================
# VARIABLES SUBMENU
# ============================================
def submenu_variables():
    while True:
        clear_screen()
        print("==== VARIABLES MENU ====")
        print("[1] Integer and String Variables")
        print("[2] User Input Example")
        print("[0] Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = "Alice"
            age = 18
            print(f"\nName: {name}")
            print(f"Age: {age}")
            input("\nPress Enter to continue...")
        elif choice == "2":
            user = input("\nEnter your name: ")
            print(f"Hello, {user}! Welcome!")
            input("\nPress Enter to continue...")
        elif choice == "0":
            return
        else:
            input("Invalid choice. Press Enter to try again...")


# ============================================
# OPERATORS SUBMENU
# ============================================
def submenu_operators():
    while True:
        clear_screen()
        print("==== OPERATORS MENU ====")
        print("[1] Arithmetic Operators")
        print("[2] Comparison Operators")
        print("[0] Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            a, b = 10, 3
            print(f"\nAddition: {a} + {b} = {a+b}")
            print(f"Division: {a} / {b} = {a/b}")
            print(f"Exponent: {a} ** {b} = {a**b}")
            input("\nPress Enter to continue...")
        elif choice == "2":
            x, y = 5, 8
            print(f"\nIs {x} > {y}?  {x > y}")
            print(f"Is {x} == {y}?  {x == y}")
            input("\nPress Enter to continue...")
        elif choice == "0":
            return
        else:
            input("Invalid choice. Press Enter to try again...")


# ============================================
# CONDITIONALS SUBMENU
# ============================================
def submenu_conditionals():
    while True:
        clear_screen()
        print("==== CONDITIONALS MENU ====")
        print("[1] If Statement Example")
        print("[2] If-Else Example")
        print("[0] Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            num = 10
            print(f"\nNumber = {num}")
            if num > 5:
                print("The number is greater than 5.")
            input("\nPress Enter to continue...")

        elif choice == "2":
            age = int(input("\nEnter your age: "))
            if age >= 18:
                print("You are an adult.")
            else:
                print("You are a minor.")
            input("\nPress Enter to continue...")
        elif choice == "0":
            return
        else:
            input("Invalid choice. Press Enter to try again...")


# ============================================
# LOOPS SUBMENU
# ============================================
def submenu_loops():
    while True:
        clear_screen()
        print("==== LOOPS MENU ====")
        print("[1] For Loop Example")
        print("[2] While Loop Example")
        print("[0] Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nFor Loop:")
            for i in range(1, 6):
                print("Count:", i)
            input("\nPress Enter to continue...")
        elif choice == "2":
            print("\nWhile Loop:")
            count = 1
            while count <= 5:
                print("Count:", count)
                count += 1
            input("\nPress Enter to continue...")
        elif choice == "0":
            return
        else:
            input("Invalid choice. Press Enter to try again...")


# ============================================
# LISTS SUBMENU
# ============================================
def submenu_lists():
    while True:
        clear_screen()
        print("==== LISTS MENU ====")
        print("[1] Display List Example")
        print("[2] Add Item to List")
        print("[0] Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            fruits = ["apple", "banana", "cherry"]
            print("\nFruit List:", fruits)
            input("\nPress Enter to continue...")
        elif choice == "2":
            fruits = []
            while True:
                item = input("Add a fruit (or type 'done'): ")
                if item.lower() == "done":
                    break
                fruits.append(item)
            print("Updated List:", fruits)
            input("\nPress Enter to continue...")
        elif choice == "0":
            return
        else:
            input("Invalid choice. Press Enter to try again...")


# ============================================
# FUNCTIONS SUBMENU
# ============================================
def submenu_functions():
    while True:
        clear_screen()
        print("==== FUNCTIONS MENU ====")
        print("[1] Simple Function")
        print("[2] Function With Parameters")
        print("[0] Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            def greet():
                print("Hello from a function!")
            greet()
            input("\nPress Enter to continue...")

        elif choice == "2":
            def add(a, b):
                return a + b

            print("\nResult =", add(10, 5))
            input("\nPress Enter to continue...")
        elif choice == "0":
            return
        else:
            input("Invalid choice. Press Enter to try again...")


# ============================================
# USER-DEFINED PYTHON CODE EXECUTION
# ============================================
def run_user_program():
    clear_screen()
    print("==== USER-DEFINED PROGRAM EXECUTION ====")
    print("Enter your Python code below.")
    print("Type 'done' on a new line to execute.\n")

    code_lines = []
    while True:
        line = input()
        if line.strip().lower() == "done":
            break
        code_lines.append(line)

    print("\n--- Output ---")
    try:
        exec("\n".join(code_lines))
    except Exception as e:
        print("Error:", e)

    input("\nPress Enter to return to Main Menu...")


# ============================================
# START PROGRAM
# ============================================
welcome_screen()
main_menu()
