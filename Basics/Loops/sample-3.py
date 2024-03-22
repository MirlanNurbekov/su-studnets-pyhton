original_string = input("Enter a string to reverse: ")

reversed_string = ""

for character in original_string[::-1]:

    reversed_string += character

print(f"Reversed string: {reversed_string}")
