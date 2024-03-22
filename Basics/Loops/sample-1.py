# Ask the user for the number n
n = int(input("Enter a number to calculate the factorials up to: "))

for i in range(1, n+1):
    factorial = 1  # Initialize the factorial variable
    for j in range(1, i+1):
        factorial *= j  # Multiply factorial by each number up to i
    print(f"The factorial of {i} is {factorial}")
