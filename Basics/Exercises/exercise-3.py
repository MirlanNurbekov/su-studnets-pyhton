def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid integer.")

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

start = get_integer_input("Enter the start of the range: ")
end = get_integer_input("Enter the end of the range: ")
message = input("Enter a message to print: ")

# Asking the user to choose if they want to print the message for even numbers, odd numbers, or all numbers
print_even = get_yes_no_input("Would you like to print the message for even numbers only? (yes/no): ")
print_odd = False if print_even else get_yes_no_input("Would you like to print the message for odd numbers only? (yes/no): ")

for number in range(start, end + 1):
    if print_even and number % 2 == 0:
        print(f"{number}: {message}")
    elif print_odd and number % 2 != 0:
        print(f"{number}: {message}")
    elif not print_even and not print_odd:
        print(f"{number}: {message}")
