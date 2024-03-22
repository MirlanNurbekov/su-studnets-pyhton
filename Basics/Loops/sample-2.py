# Ask the user to enter the starting and ending numbers of the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")

for number in range(start, end + 1):
    # Prime numbers are greater than 1
    if number > 1:
        # Assume number is prime until shown it is not
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                is_prime = False
                break  # No need to continue; it's not prime
        if is_prime:
            print(number, end=" ")
