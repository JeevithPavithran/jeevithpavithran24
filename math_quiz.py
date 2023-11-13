import random


def random_number(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def random_operator():
    return random.choice(['+', '-', '*'])


def calculation(number1, number2, operator):
    problem = f"{number1} {operator} {number2}"
    if operator == '+': answer = number1 + number2
    elif operator == '-': answer = number1 - number2
    else: answer = number1 * number2
    return problem, answer

def math_quiz():
    score = 0
    no_of_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(no_of_questions):
        number1 = random_number(1, 10); number2 = random_number(1, 5); operator = random_operator()

        PROBLEM, ANSWER = calculation(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{no_of_questions}")

if __name__ == "__main__":
    math_quiz()
