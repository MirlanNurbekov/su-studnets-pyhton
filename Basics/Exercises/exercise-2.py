def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def get_order(start, end):
    return 1 if start <= end else -1

start = get_integer_input("Enter the start of the range: ")
end = get_integer_input("Enter the end of the range: ")
message = input("Enter a message to print with each number: ")
special_number = get_integer_input("Enter a special number to apply a unique message: ")
special_message = input("Enter the special message: ")

order = get_order(start, end)

for number in range(start, end + order, order):
    if number == special_number:
        print(f"{number}: {special_message}")
    else:
        print(f"{number}: {message}")