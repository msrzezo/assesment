# checking user enters yes / no (takes in a question)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''

**** instructions ****
  
To begin the maths quiz, choose the amount of questions
you would like to answer and what difficulty you want 
(Easy, medium, hard, impossible) try to beat impossible level!
Good Luck!
To stop the game at any point, type `xxx`

Good Luck!

    ''')


# Main Routine
print()
print("➗➖MATH QUIZ✖️➕ ")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions? ")

# checks user enters yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")
