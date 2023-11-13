import random

def random_integer(min_val, max_val):
    """
    Generates a random integer within the specified range.
    """
    return random.randint(min_val, max_val)

def random_operator():
    """
    Generates a random arithmetic operator among '+', '-', '*'.
    """
    return random.choice(['+', '-', '*'])

def operation(num1, num2, operator):
    """
    Performs the arithmetic operation based on the operator provided.
    Returns the problem string and the answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = random_integer(1, 10)
        num2 = random_integer(1, 5)
        operator = random_operator()

        problem, correct_answer = operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
