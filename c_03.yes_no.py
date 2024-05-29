# checking user enters yes / no (takes in a question)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes/no ")


# Main Routine
print("➗➖MATH QUIZ✖️➕")
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"program continues ")


