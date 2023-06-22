import os
import time

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the menu options
def display_menu():
    print("=== Calculator ===")
    print("1. Weight Conversion")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

# Function to execute the selected option
def execute_option(option):
    clear_screen()
    if option == 1:
        print("Opening Weight Conversion...")
        time.sleep(3)
        # Call the Python file corresponding to Option 1
        os.system("python Weightconversion.py")
    elif option == 2:
        print("Opening Option 2...")
        time.sleep(3)
        # Call the Python file corresponding to Option 2
        os.system("python option2.py")
    elif option == 3:
        print("Executing Option 3...")
        time.sleep(3)
        # Call the Python file corresponding to Option 3
        os.system("python option3.py")
    elif option == 4:
        print("Exiting...")
        time.sleep(3)
        exit()
    else:
        print("Invalid option!")

# Main menu loop
while True:
    clear_screen()
    display_menu()
    choice = input("Select an option: ")
    try:
        choice = int(choice)
        execute_option(choice)
    except ValueError:
        print("Invalid option!")
