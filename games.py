import os
import time

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the menu options
def display_menu():
    print("=== GAMES ===")
    print("1. Snake")
    print("2. Rock Paper Scissors")
    print("3. Hangman")
    print("4. Exit")

# Function to execute the selected option
def execute_option(option):
    if option == 1:
        clear_screen()
        print("Opening Snake...")
        time.sleep(3)
        # Call the Python file corresponding to Option 1
        os.system("python snake.py")
    elif option == 2:
        clear_screen()
        print("Opening Rock Paper Scissors...")
        time.sleep(3)
        # Call the Python file corresponding to Option 2
        os.system("python rockpaperscissors.py")
    elif option == 3:
        clear_screen()
        print("Opening Hangman...")
        time.sleep(3)
        # Call the Python file corresponding to Option 3
        os.system("python hangman.py")
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
