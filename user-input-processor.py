# Task 1: Input Length Validator

# Creating an infinite loop that will only break once the user inputs a valid first and last name
while True:
    name_input = input("Enter your first and last name: ").title()
    split_names = name_input.split(" ")
    if len(split_names) == 2:
        first_name, last_name = split_names
        if first_name.isalpha() and last_name.isalpha():
            if len(first_name) >= 2 and len(last_name) >= 2:
                print(f"{name_input} is a valid name.")
                break
            else:
                print("Invalid name. Please enter your full name.\n")
        else:
            print("Invalid name. Please enter your full name.\n")
    else:
        print("Invalid name. Please enter your full name.\n")