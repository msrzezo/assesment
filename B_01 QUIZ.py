import random


#  yes/no question and return True for yes, False for no
def yes_no(question):
    while True:
        response = input(question).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


# Function to generate a random equation and its correct answer based on difficulty level
def generate_equation_and_answer(difficulty_level):
    if difficulty_level == 'easy':
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        operators = ["+", "-"]  # easy
    elif difficulty_level == 'medium':
        num1, num2 = random.randint(10, 25), random.randint(10, 25)
        operators = ["+", "-", "*"]  # medium
    elif difficulty_level == 'hard':
        num1, num2 = random.randint(25, 50), random.randint(25, 50)
        operators = ["*", "/"]  # hard
    else:
        num1, num2 = random.randint(25, 75), random.randint(25, 75)
        operators = ["*", "/"]  # impossible

    operator = random.choice(operators)
    if operator == "+":
        return f"{num1} + {num2}", num1 + num2
    elif operator == "-":
        return f"{max(num1, num2)} - {min(num1, num2)}", abs(num1 - num2)
        # ⬆️⬆️⬆️⬆️ makes sure there is no negative number in the answer by putting the larger number first
    elif operator == "*":
        return f"{num1} * {num2}", num1 * num2
    else:
        return f"{num1 * num2} / {num2}", num1
        # ⬆️⬆️ makes sure there is no decimal answers


# Function for a single question of the quiz
def quiz_question(difficulty_level, quiz_history):
    emoji_correct = "✔️"
    emoji_incorrect = "❌"
    emoji_equation = "🔢"
    while True:
        equation, correct_answer = generate_equation_and_answer(difficulty_level)
        print(f"\n{emoji_equation} Here's your question (Difficulty: {difficulty_level}):")
        print(f"Equation: {equation}")

        while True:
            user_input = input("Your answer: ").strip().lower()
            if user_input == "xxx":
                if yes_no("Are you sure you want to quit? "):
                    return -2
                else:
                    continue  # Ask the same question again if the user wants to continue
            if user_input == "":
                print("Invalid input. Please enter an answer.")
                continue
            try:
                user_answer = int(user_input)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

        quiz_history.append((equation, user_answer, correct_answer))
        if user_answer == correct_answer:
            print(f"Correct! {emoji_correct}")
            return 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}. {emoji_incorrect}")
            return 0


# Main function to run the quiz
def quiz():
    # Asking user for number of questions and difficulty level
    while True:
        questions_input = input(
            "How many questions would you like to answer? (Press Enter for infinite questions): ").strip()
        if questions_input == "":
            questions = float('inf')
            print("∞ Infinite Mode ∞ 🕹️🌀")
            break
        try:
            questions = int(questions_input)
            if questions == 0:
                print("Please enter a valid number of questions.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number of questions.")

    # difficulty level inputs lists
    difficulty_levels = {'e': 'easy', 'easy': 'easy', 'm': 'medium', 'medium': 'medium', 'h': 'hard', 'hard': 'hard',
                         'i': 'impossible', 'impossible': 'impossible'}
    while True:
        difficulty_input = input("Choose the difficulty level ( Easy, Medium, Hard, Impossible): ").strip().lower()
        if difficulty_input in difficulty_levels:
            difficulty_level = difficulty_levels[difficulty_input]
            break
        else:
            print("Invalid input. Please choose a valid difficulty level.")

    # variables for score and quiz history
    questions_right = 0
    quiz_history = []
    questions_asked = 0

    # Loop for asking questions until user decides to stop or reach the specified number of questions
    while True:
        if questions != float('inf') and questions_asked == questions:
            break
        score = quiz_question(difficulty_level, quiz_history)
        if score == -2:
            break
        questions_asked += 1
        questions_right += score  # Increment score regardless of correctness

    # final score and quiz history
    print("\nQuiz over!")
    print(f"Questions right: {questions_right}/{questions_asked}")
    if questions_asked > 0 and questions_asked == questions_right:
        print("\nYay! Good job, you got all of the questions right!")

    if quiz_history:
        if yes_no("Do you want to see the quiz history? "):
            print("\nQuiz History:")
            for i, (equation, user_answer, correct_answer) in enumerate(quiz_history, start=1):
                print(f"Question {i}:")
                print(f" Equation: {equation}")
                print(f" Your Answer: {user_answer}")
                print(f" Correct Answer: {correct_answer}")

    # Asking user if they want to play again
    if yes_no("Do you want to answer more questions? "):
        quiz()
    else:
        print("Thank you for answering questions!")


# Main routine to start the quiz
print()
print("➗➖MATH QUIZ✖️➕")
print()
if yes_no("Do you want to read the instructions? "):
    print("""
    **** instructions ****
    To begin the maths quiz, choose the amount of questions
    you would like to answer and what difficulty you want 
    (Easy, Medium, Hard, Impossible) try to beat impossible level!
    Good Luck!
    To stop the quiz at any point, type `xxx`""")
quiz()
