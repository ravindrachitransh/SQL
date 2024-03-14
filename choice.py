def clear_screen():
    if os.name == 'nt':
        # For Windows, print 100 empty lines to simulate clearing the screen
        print('\n' * 100)
    else:
        # For other platforms, use the 'clear' command
        os.system('clear')


import os



def print_menu():
    # clear_screen()

    # Define the menu options
    menu = [
        "1. Get the statististical analysis of Age vs Deaths  ",
        "2. Get the statististical analysis of Ethnicity vs Deaths",
        "3. Get the statististical analysis of Medical_condition vs Deaths",
        "4. Get the statististical analysis of ICU_type vs Deaths",
        "5. Get the statististical analysis of BMI vs Deaths",
        "0. Exit"
    ]

    # Get terminal size with fallback to default values
    try:
        screen_width = os.get_terminal_size().columns
    except OSError:
        # Default values if terminal size cannot be obtained
        screen_width = 80

    menu_width = max(len(line) for line in menu)
    margin = (screen_width - menu_width) // 2

    # Clear screen and print menu
    print("\n" * (os.get_terminal_size().lines // 3))
    print(" " * margin + "CHOICE MENU")
    print("-" * screen_width)

    for line in menu:
        print(" " * margin + line)

    print("-" * screen_width)




def show_menu():
    

    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice (0-5): "))
            if choice in [0, 1, 2, 3, 4, 5]:
                # if choice == 0:
                #     clear_screen()
                #     print("Goodbye!")
                #     break
                break  # Exit the loop if the choice is valid
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    
        

    return choice
show_menu()
