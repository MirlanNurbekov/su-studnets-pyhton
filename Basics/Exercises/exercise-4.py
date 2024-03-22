def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid integer.")

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_range_with_condition(start, end, condition_func, message):
    for number in range(start, end + 1):
        if condition_func(number):
            print(f"{number}: {message}")

def main_menu():
    print("\n1. Print even numbers")
    print("2. Print odd numbers")
    print("3. Print prime numbers")
    print("4. Exit")
    return get_integer_input("Choose an option: ")

def main():
    start = get_integer_input("Enter the start of the range: ")
    end = get_integer_input("Enter the end of the range: ")

    while True:
        choice = main_menu()
        if choice == 1:
            print_range_with_condition(start, end, lambda x: x % 2 == 0, "Even")
        elif choice == 2:
            print_range_with_condition(start, end, lambda x: x % 2 != 0, "Odd")
        elif choice == 3:
            print_range_with_condition(start, end, is_prime, "Prime")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
