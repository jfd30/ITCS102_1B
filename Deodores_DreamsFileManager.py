import os

def display_menu():
    """Prints the main menu options to the console."""
    print("\n==== DREAMS FILE MANAGER ====")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

def read_messages(filename):
    """Reads and displays all lines from the text file."""
    print("\n--- Inspiring Messages ---")
    try:
        with open(filename, "r") as file:
            content = file.read()
            if content.strip():
                print(content)
            else:
                print("The file is currently empty.")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

def add_message(filename):
    """Appends a new user-provided message to the end of the file."""
    new_message = input("Enter your new inspiring line: ")
    try:
        with open(filename, "a") as file:
            # Ensure the new message starts on a new line
            file.write("\n" + new_message)
        print("Your inspiration has been added!")
    except Exception as e:
        print(f"An error occurred: {e}")

def rewrite_file(filename):
    """Overwrites the existing file with new content after user confirmation."""
    confirm = input("Are you sure you want to rewrite the entire file? (yes/no): ").lower()
    if confirm == 'yes':
        new_content = input("Enter the new content for the file:\n")
        try:
            with open(filename, "w") as file:
                file.write(new_content)
            print("The file has been rewritten successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Operation cancelled.")

def main():
    # Use the filename provided in your instructions
    filename = "dreams.txt"

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            read_messages(filename)
        elif choice == '2':
            add_message(filename)
        elif choice == '3':
            rewrite_file(filename)
        elif choice == '4':
            print("Exiting program... Stay inspired!")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
