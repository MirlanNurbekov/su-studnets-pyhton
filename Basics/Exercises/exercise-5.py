import random

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid integer.")

def generate_arithmetic_problem():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)
    correct_answer = eval(f"{num1} {operation} {num2}")
    return num1, operation, num2, correct_answer

def quiz():
    score = 0
    total_questions = 5
    for _ in range(total_questions):
        num1, operation, num2, correct_answer = generate_arithmetic_problem()
        user_answer = get_integer_input(f"What is {num1} {operation} {num2}? ")
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    
    print(f"Quiz completed. Your score: {score}/{total_questions}")
    if score == total_questions:
        print("Excellent work!")
    elif score >= total_questions / 2:
        print("Good job, but you can do better!")
    else:
        print("Keep practicing!")

if __name__ == "__main__":
    quiz()
