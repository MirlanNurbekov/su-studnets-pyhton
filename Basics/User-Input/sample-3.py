def get_age_input():
    while True:
        try:
            age = int(input("How old are you? "))
            if age < 0:
                print("Please enter a valid age.")
            else:
                return age
        except ValueError:
            print("Please enter a numeric value.")

age = get_age_input()

if age < 16:
    print("You are too young for the voting or driving license eligibility.")
elif 16 <= age < 18:
    print("You may be eligible for a driving permit, depending on your jurisdiction.")
    print("However, you are not eligible to vote yet.")
elif 18 <= age < 21:
    print("You are eligible to vote.")
    print("You may be eligible for a driving license, depending on your jurisdiction.")
    print("You are not of legal drinking age in some countries.")
elif 21 <= age < 65:
    print("You are eligible to vote, drive, and in most countries, legally consume alcohol.")
    print("Consider regular health check-ups.")
else:
    print("You are eligible for all the previously mentioned activities.")
    print("If you haven't started already, it might be a good time to look into retirement planning.")

