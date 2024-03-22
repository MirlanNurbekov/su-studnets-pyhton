start = int(input("Enter the start of the range: "))

end = int(input("Enter the end of the range: "))

message = input("Enter a message to print with each number: ")

for number in range(start, end + 1):
    print(f"{number}: {message}")