"""This a quiz that tests knowledge on anime."""
__author__ = "Jorge Cano"

# This a quiz that tests knowledge on anime.
print("Welcome, this quiz will test your knowledge on 3 different shows")
print("Your score will be shown after you finish.")
ready_yn = input("To begin press y:")
print("Quiz 1: Naruto")
naru_score = 0  # Accumulator for the first quiz.
naru_retry = True
# This line of code loops back to the beginning of the first quiz
while naru_retry:
    naru_score = 0
    print("Q#1: 'What S-rank jutsu did Naruto invent?'")
    print("1. Rasenshuriken\n2. Flying Raijin\n3. Lightning Blade\n4. Kirin")
    while True:  # Loops back to the input for this question.
        try:
            naru_ans1 = int(input("Please enter a number from 1-4: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if naru_ans1 == 1:
        print("Correct!")
        naru_score += 1
    elif naru_ans1 != 1:
        print("Incorrect.")
        naru_score += 0
    print("Q#2: 'Which abilities does Itachi's MS have?'")
    print("1. Tsukuyomi\n2. Kamui\n3. Kotoamatsukami\n4. Amaterasu")
    print("Please provide two answers. Enter numbers from 1-4")
    while True:  # Loops back to the input for this question.
        try:
            naru_ans2 = int(input("Select the first answer: "))
            naru_ans2_ = int(input("Select the second answer: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if naru_ans2 == 1 and naru_ans2_ == 4:
        print("Correct!")
        naru_score += 2
    elif naru_ans2 == 1 or 4:
        print("Close, but not quite.")
        naru_score += 1
    else:
        print("Incorrect.")
    print("Q#3: 'What is Tobi's real name?")
    print("1. Madara\n2. Obito\n3. Zetsu\n4. Nagato")
    while True:  # Loops back to the input for this question.
        try:
            naru_ans3 = int(input("Please enter a number from 1-4: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if not (naru_ans3 == 2):
        print("Incorrect")
        naru_score += 0
    elif naru_ans3 == 2:
        print("Correct!")
        naru_score += 1
    print("Q#4: 'Minato Naamikaze invented the Reaper Death Seal.'")
    while True:  # Loops back to the input for this question.
        try:
            naru_ans4 = int(input("1. True or 2. False?: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-2")
    if naru_ans4 == 1:
        print("Correct!")
        naru_score += 1
    elif naru_ans4 == 2:
        naru_score += 0
    else:
        naru_score += 0
    print("Your score for this quiz is: ", naru_score, "/5", sep='')
    naru_redo = input("If you would like to try again press 'y': ")
    # This line of code determines whether the quiz will loop or move on.
    if naru_redo != 'y':
        naru_retry = False
print("Continuing to next quiz.")
print("Quiz 2: Cowboy Bebop")
bebop_score = 0  # Accumulator for the second quiz.
bebop_retry = True
# Ths line loops back to the beginning of the second quiz
while bebop_retry:
    bebop_score = 0
    print("Q#1: What is the name of the crew's ship?")
    print("1. Hammer Head\n2. Swordfish II\n3. The Bebop\n4. Red Tail")
    while True:  # Loops back to the input for this question.
        try:
            bebop_ans1 = int(input("Please enter a number from 1-4: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if bebop_ans1 == 3:
        print("Correct!")
        bebop_score += 1
    else:
        bebop_score += 0
    print("Q#2: What song plays while Spike flies through the window in ep.5?")
    print("1.Fantaisie Sign\n2. Green Bird\n3. Space Lion\n4. Cats on Mars")
    while True:  # Loops back to the input for this question.
        try:
            bebop_ans2 = int(input("Please enter a number from 1-4: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if bebop_ans2 == 2:
        print("Correct!")
        bebop_score += 1
    else:
        bebop_score += 0
    print("Q#3 Which character was the plot focused on in Ganymede Elegy?")
    print("1. Jet\n2. Spike\n3. Faye\n4. Ed")
    while True:  # Loops back to the input for this question.
        try:
            bebop_ans3 = int(input("Please enter a number from 1-4: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if bebop_ans3 == 1:
        print("Correct!")
        bebop_score += 1
    else:
        bebop_score += 0
    print("Q#4: Which character nearly killed Spike in their first encounter?")
    print("1. Mad Pierrot\n2. Asimov\n3. Abdul Hakim\n4. Andy Von De Oniyate")
    while True:  # Loops back to the input for this question.
        try:
            bebop_ans4 = int(input("Please enter a number from 1-4: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if bebop_ans4 == 1:
        print("Correct!")
        bebop_score += 1
    else:
        bebop_score += 0
    print("Q#5: Dr. Londes is the leader of the cult SCRATCH")
    while True:  # Loops back to the input for this question.
        try:
            bebop_ans5 = int(input("1. True or 2. False?"))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-2")
    if bebop_ans5 == 1:
        print("Correct!")
        bebop_score += 1
    elif bebop_ans5 == 2:
        bebop_score += 0
    else:
        bebop_score += 0
    print("Your score for this quiz is: ", bebop_score, "/5", sep='')
    bebop_redo = input("If you would like to try again press 'y': ")
    # This line of code determines whether the quiz will loop or move on.
    if bebop_redo != 'y':
        bebop_retry = False
print("Continuing to next quiz.")
print("Quiz 3: Fullmetal Alchemist Brotherhood")
fmab_score = 0
fmab_retry = True
# This line of code loops back to the beginning of the third quiz
while fmab_retry:
    fmab_score = 0
    print("Q#1: Ed is called 'Fullmetal' because he has metal limbs.")
    print("1. True or 2. False?")
    while True:  # Loops back to the input for this question.
        try:
            fmab_ans1 = int(input("Please enter a number from 1-2: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if fmab_ans1 == 1:
        print("Correct!")
        fmab_score += 1
    elif fmab_ans1 == 2:
        fmab_score += 0
    else:
        fmab_score += 0
    print("Q#2: What is Ed's occupation?")
    print("1. Scientist\n2. Alchemist\n3. Politician\n4. Police Officer")
    while True:  # Loops back to the input for this question.
        try:
            fmab_ans2 = int(input("Please enter a number from 1-4: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if fmab_ans2 == 2:
        print("Correct!")
        fmab_score += 1
    else:
        fmab_score += 0
    print("Q#3: Which of the following Characters have Xerxesian ancestry: ")
    print("1. Van Hoenheim\n2. Alphonse Elric\n3. Roy Mustang\n4.Scar")
    while True:  # Loops back to the input for this question.
        try:
            fmab_ans3 = int(input("Select the first answer"))
            fmab_ans3_ = int(input("Select the second answer"))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if fmab_ans3 == 1 and fmab_ans3_ == 2:
        print("Correct!")
        fmab_score += 2
    elif fmab_ans3 == 1 or 2:
        print("Close, but not quite.")
        fmab_score += 1
    else:
        print("Incorrect.")
    print("Q#4: Who is the main antagonist in the series?")
    print("1. Bradley\n2. Pride\n3. Greed\n4. Father")
    while True:  # Loops back to the input for this question.
        try:
            fmab_ans4 = int(input("Please enter a number from 1-4: "))
            break  # Breaks the loop when a number is input.
        except ValueError:  # Starts the loop if the input is not a number.
            print("Error, please enter a number from 1-4")
    if fmab_ans4 == 4:
        print("Correct!")
        fmab_score += 1
    else:
        print("Incorrect")
    print("Your score for this quiz is: ", fmab_score, "/5", sep='')
    fmab_redo = input("If you would like to try again press 'y': ")
    # This line of code determines whether the quiz will loop or move on.
    if fmab_redo != 'y':
        fmab_retry = False


# This function find the average score across each quiz.
def average():
    total_score = naru_score + bebop_score + fmab_score
    average_score = total_score / 3  # Calculates the average score.
    return average_score


# This function calls the function average and prints a string.
def main():
    print("Your average score is ", format(average(), "0.2f"))


final_score = naru_score + bebop_score + fmab_score
print("Your total score across the 3 quizzes is ", final_score, "/15", sep='')
# These lines print the word perfect multiple times if the total score is 15.
if final_score == 15:
    for x in range(3):
        for i in range(3):
            print("PERFECT!" + " ", end=" ")
        print()
main()
