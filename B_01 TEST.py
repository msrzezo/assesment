import random


def yes_no(question):
    while True:
        response = input(question).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def generate_equation_and_answer(difficulty_level):
    if difficulty_level == 'easy':
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        operators = ["+", "-"]
    elif difficulty_level == 'medium':
        num1, num2 = random.randint(10, 25), random.randint(10, 25)
        operators = ["+", "-", "*"]
    elif difficulty_level == 'hard':
        num1, num2 = random.randint(25, 100), random.randint(25, 50)
        operators = ["-", "*", "/"]
    else:  # impossible
        num1, num2 = random.randint(25, 100), random.randint(50, 100)
        operators = ["*", "/"]

    operator = random.choice(operators)
    if operator == "+":
        return f"{num1} + {num2}", num1 + num2
    elif operator == "-":
        return f"{max(num1, num2)} - {min(num1, num2)}", abs(num1 - num2)
    elif operator == "*":
        return f"{num1} * {num2}", num1 * num2
    else:  # operator == "/"
        return f"{num1 * num2} / {num2}", num1


def quiz_round(difficulty_level, game_history):
    emoji_correct = "✔️"
    emoji_incorrect = "❌"
    emoji_equation = "🔢"
    equation, correct_answer = generate_equation_and_answer(difficulty_level)
    print(f"\n{emoji_equation} Here's your question (Difficulty: {difficulty_level}):")
    print(f"Equation: {equation}")

    while True:
        user_input = input("Your answer: ").strip().lower()
        if user_input == "xxx":
            return -2
        if user_input == "":
            print("Invalid input. Please enter an answer.")
            continue
        try:
            user_answer = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

    game_history.append((equation, user_answer, correct_answer))
    if user_answer == correct_answer:
        print(f"Correct! {emoji_correct}")
        return 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}. {emoji_incorrect}")
        return 0


def quiz():
    while True:
        rounds_input = input("How many questions would you like to answer? (Press Enter for infinite rounds): ").strip()
        if rounds_input == "":
            rounds = float('inf')
            print("∞ Infinite Mode ∞ 🕹️🌀")
            break
        try:
            rounds = int(rounds_input)
            if rounds == 0:
                print("Please enter a valid number of rounds.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number of questions.")

    difficulty_levels = {'easy': 'easy', 'medium': 'medium', 'hard': 'hard', 'impossible': 'impossible'}
    while True:
        difficulty_input = input("Choose the difficulty level (easy, medium, hard, impossible): ").strip().lower()
        if difficulty_input in difficulty_levels:
            difficulty_level = difficulty_levels[difficulty_input]
            break
        else:
            print("Invalid input. Please choose a valid difficulty level.")

    total_score = 0
    game_history = []
    questions_asked = 0
    while True:
        if rounds != float('inf') and questions_asked == rounds:
            break
        score = quiz_round(difficulty_level, game_history)
        if score == -2:
            break
        if score != -1:
            questions_asked += 1
        total_score += score

    print("\nGame over!")
    print(f"Total Score: {total_score}/{questions_asked}")
    if total_score == questions_asked:
        print("\nYay! Good job, you got all of the questions right!")

    if game_history:
        if yes_no("Do you want to see the quiz history? "):
            print("\nQuiz History:")
            for i, (equation, user_answer, correct_answer) in enumerate(game_history, start=1):
                print(f"Round {i}:")
                print(f" Equation: {equation}")
                print(f" Your Answer: {user_answer}")
                print(f" Correct Answer: {correct_answer}")

    if yes_no("Do you want to answer more questions? "):
        quiz()
    else:
        print("Thank you for playing!")


# main routine
print()
print("➗➖MATH QUIZ✖️➕")
print()
if yes_no("Do you want to read the instructions? "):
    print("""
    **** instructions ****
    To begin the maths quiz, choose the amount of questions
    you would like to answer and what difficulty you want 
    (Easy, medium, hard, impossible) try to beat impossible level!
    Good Luck!
    To stop the game at any point, type `xxx`""")
quiz()
