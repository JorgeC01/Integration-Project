#Jorge Cano
#This a quiz that tests knowledge on anime.
print("Welcome, this quiz will test your knowledge on 3 different shows")
print("Your score will be shown after you finish.")
ready_yn = input("To begin press y:")
print("Quiz 1: Naruto")
naru_score = 0
naru_retry = True
#This line of code loops back to the beginning of the first quiz
while naru_retry:
    naru_score = 0
    print("Q#1: 'What S-rank jutsu did Naruto invent?'")
    print("a. Rasenshuriken\nb. Flying Raijin\nc. Lightning Blade\nd. Kirin")
    naru_ans1 = input()
    if naru_ans1 == 'a':
        print("Correct!")
        naru_score += 1
    elif naru_ans != a:
        print("Incorrect.")
        naru_score += 0
    print("Q#2: 'Which abilities does Itachi's MS have?'")
    print("a. Tsukuyomi\nb. Kamui\nc. Kotoamatsukami\nd. Amaterasu")
    naru_ans2 = input("Select 2 answers:")
    naru_ans2_ = input()
    if naru_ans2 == 'a' and naru_ans2_ == 'd':
        print("Correct!")
        naru_score += 2
    elif naru_ans2 == 'a' or 'd':
        print("Close, but not quite.")
        naru_score += 1
    else:
        print("Incorrect.")
    print("Q#3: 'What is Tobi's real name?")
    print("a. Madara\nb. Obito\nc. Zetsu\nd. Nagato")
    naru_ans3 = input()
    if not(naru_ans3 == 'b'):
        print("Incorrect")
        naru_score += 0
    elif naru_ans3 == 'b':
        print("Correct!")
        naru_score += 1
    print("Q#4: 'Minato Naamikaze invented the Reaper Death Seal.'")
    naru_ans4 = input("True or False?: ")
    if naru_ans4 == 'true':
        print("Correct!")
        naru_score += 1
    elif naru_ans4 == 'false':
        naru_score += 0
    print("Your score for this quiz is: ", naru_score ,"/5", sep='')
    naru_redo = input("If you would like to try again press 'y': ")
    #This line of code determines whether the quiz will loop or move on.
    if naru_redo != 'y':
        naru_retry = False
print("Continuing to next quiz.")
print("Quiz 2: Cowboy Bebop")
bebop_score = 0
bebop_retry = True
#Ths line loops back to the beginning of the second quiz
while bebop_retry:
    bebop_score = 0
    print("Q#1: What is the name of the crew's ship?")
    print("a. Hammer Head\nb. Swordfish II\nc. The Bebop\nd. Red Tail")
    bebop_ans1 = input()
    if bebop_ans1 == 'c':
        print("Correct!")
        bebop_score += 1
    else:
        bebop_score += 0
    print("Q#2: What song plays while Spike flies through the window in ep.5?")
    print("a.Fantaisie Sign\nb. Green Bird\nc. Space Lion\nd. Cats on Mars")
    bebop_ans2 = input()
    if bebop_ans2 == 'b':
        print("Correct!")
        bebop_score += 1
    else:
        bebop_score += 0
    print("Q#3 Which character was the plot focused on in Ganymede Elegy?")
    print("a. Jet\nb. Spike\nc. Faye\nd. Ed")
    bebop_ans3 = input()
    if bebop_ans3 == 'a':
        print("Correct!")
        bebop_score += 1
    else:
        bebop_score += 0
    print("Q#4: Which character nearly killed Spike in their first encounter?")
    print("a. Mad Pierrot\nb. Asimov\nc. Abdul Hakim\nd. Andy Von De Oniyate")
    bebop_ans4 = input()
    if bebop_ans4 == 'a':
        print("Correct!")
        bebop_score += 1
    else:
        bebop_score += 0
    print("Q#5: Dr. Londes is the leader of the cult SCRATCH")
    print("True or False?")
    bebop_ans5 = input()
    if bebop_ans5 == 'true':
        print("Correct!")
        bebop_score += 1
    elif bebop_ans5 == 'false':
        bebop_score += 0
    print("Your score for this quiz is: ", bebop_score ,"/5", sep='')
    bebop_redo = input("If you would like to try again press 'y': ")
    #This line of code determines whether the quiz will loop or move on.
    if bebop_redo != 'y':
        bebop_retry = False
print("Continuing to next quiz.")
print("Quiz 3: Fullmetal Alchemist Brotherhood")
fmab_score = 0
fmab_retry = True
#This line of code loops back to the beginninng of the third quiz
while fmab_retry:
    fmab_score = 0
    print("Q#1: Ed is called 'Fullmetal' because he has metal limbs.")
    print("True or False?")
    fmab_ans1 = input()
    if fmab_ans1 == 'true':
        print("Correct!")
        fmab_score += 1
    elif fmab_ans1 == 'false':
        fmab_score += 0
    print("Q#2: What is Ed's occupation?")
    print("a. Scientist\nb. Alchemist\nc. Politician\nd. Police Officer")
    fmab_ans2 = input()
    if fmab_ans2 == 'b':
        print("Correct!")
        fmab_score += 1
    else:
        fmab_score += 0
    print("Q#3: Which of the following Characters have Xerxesian ancestry: ")
    print("a. Van Hoenheim\nb. Alphonse Elric\nc. Roy Mustang\nd.Scar")
    fmab_ans3 = input("Select all that apply: ")
    fmab_ans3_ = input()
    if fmab_ans3 == 'a' and fmab_ans3_ == 'b':
        print("Correct!")
        fmab_score += 2
    elif fmab_ans3 == 'a' or 'b':
        print("Close, but not quite.")
        fmab_score += 1
    else:
        print("Incorrect.")
    print("Q#4: Who is the main antagonist in the series?")
    print("a. Bradley\nb. Pride\nc. Greed\nd. Father")
    fmab_ans4 = input()
    if fmab_ans4 == 'd':
        print("Correct!")
        fmab_score += 1
    else:
        print("Incorrect")
    print("Your score for this quiz is: ", fmab_score ,"/5", sep='')
    fmab_redo = input("If you would like to try again press 'y': ")
    #This line of code determines whether the quiz will loop or move on.
    if fmab_redo != 'y':
        fmab_retry = False
total_score = naru_score + bebop_score + fmab_score
#This function find the average score across each quiz.
def average(total_score):
    average_score = total_score / 3
    return average_score
#This function calls the function average and prints a string.
def main():
    print("Your average score is ", format(average(total_score), "0.2f"))
print("Your total score across the 3 quizzes is ", total_score,"/15", sep='')
#These lines print the word perfect multiple times if the total score is 15. 
if total_score == 15:
    for x in range(3):
        for x in range(3):
            print("PERFECT!" + " ", end=" ")
        print()
main()
