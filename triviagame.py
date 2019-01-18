import random
import time
rung_number = 1

name = input("Welcome to Trivia Ladder! What's your name? ")
print(f"Hello, {name}! The object of the game is to use your *worldly knowledge* to climb your way to the top! There are two basic categories: WORLD and SCIENCE. At each rung of the ladder, a category will be selected at random, and a multiple-choice question will be asked. Answer correctly, and you will move up one rung. Answer incorrectly, and you will move down on the ladder. Questions will become progressively more difficult. Make it all the way to Rung 15, and you win! Fall off the ladder, and you lose!")
mode = input("Would you like to play on EASY, MEDIUM, or HARD mode?")
valid_options = ["e", "easy", "m", "medium", "h", "hard"]

while mode.lower() not in valid_options:
    mode = input("That was an invalid input. Choose from easy, medium, or hard.")
if mode.lower() == "e" or mode.lower() == "easy":
    fall_number = 2
elif mode.lower() == "m" or mode.lower() == "medium":
    fall_number = 5
elif mode.lower() == "h" or mode.lower() == "hard":
    fall_number = 10

print(f"You will fall {fall_number} rungs each time you answer incorrectly. ")
ready_to_play = input("Are you ready to play? ")

if ready_to_play.lower() == "yes" or ready_to_play.lower() == "y":
    print("Great! Let's begin...")
else:
    print("Oh well... We're still going to begin.")

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

easy_world_questions = [
    "How do you say 'good morning' in Italian?\n(a) Buona notte\n(b) Buenas noches\n(c) Buongiorno\n(d) Boa noite",
    "How do you say 'hunger' in Spanish?\n(a) Hombre\n(b) Hambre\n(c) Hungre\n(d) Humbre",
    "What is 'welcome' in French?\n(a) Bienvenue\n(b) Bienvenido\n(c) Bienvienue\n(d) Bienvena",
    "Which of these countries DOES NOT border Italy?\n(a) France\n(b) Austria\n(c) Slovenia\n(d) Germany",
    "Which of these places is NOT an actual country?\n(a) Bhutan\n(b) Maltas\n(c) Burundi\n(d) Nauru",
    "Which of these places IS a country as recognized by \n(a) \n(b) \n(c) \n(d) ",
]


ew1 = Question(easy_world_questions[0], "c")
ew2 = Question(easy_world_questions[1], "b")
ew3 = Question(easy_world_questions[2], "a")
ew4 = Question(easy_world_questions[3], "d")
ew5 = Question(easy_world_questions[4], "b")
ew6 = Question(easy_world_questions[5], "c")

easy_world_answers = [ew1, ew2, ew3, ew4, ew5, ew6]

easy_science_questions = [
    "Which of these organelles is the powerhouse of the cell?\n(a) Golgi apparatus\n(b) Nucleus\n(c) Peroxisomes\n(d) Mitochondria",
    "Which of these macromolecules stores the most energy?\n(a) nucleic acids\n(b) lipids\n(c) carbohydrate\n(d) protein",
    "guiiugguyl?\n(a) thing1\n(b) thing2",
    "dtmedy\n(a) thing1\n(b) thing2",
    "himedu\n(a) thing1\n(b) thing2",
    "hdtdmedty\n(a) thing1\n(b) thing2",
]

es1 = Question(easy_science_questions[0], "d")
es2 = Question(easy_science_questions[1], "b")
es3 = Question(easy_science_questions[2], "a")
es4 = Question(easy_science_questions[3], "a")
es5 = Question(easy_science_questions[4], "b")
es6 = Question(easy_science_questions[5], "a")


easy_science_answers = [es1, es2, es3, es4, es5, es6]

medium_world_questions = [
    "What is the capital of Venezuela?\n(a) Caracas\n(b) Asunción\n(c) Quito\n(d) Montevideo",
    "Which of these cities is not in Turkey?\n(a) Gaziantep \n(b) Ankara \n(c) Istanbul \n(d) Patras",
    "How do you say “bye” in Portuguese?\n(a) tchau \n(b) adios \n(c) adieu \n(d) te vuelvas",
    "Which of these countries borders Thailand?\n(a) China\n(b) Vietnam \n(c) Cambodia \n(d) Singapore",
    "Which of these countries is NOT in Central America?\n(a) Belize\n(b) Costa Rica\n(c) Cuba\n(d) Guatemala",
    "Which of these countries is NOT located in Asia?\n(a) Sri Lanka\n(b) Bahrain\n(c) Algeria\n(d) Myanmar",
]

medium_world_answers = [
    Question(medium_world_questions[0], "a"),
    Question(medium_world_questions[1], "d"),
    Question(medium_world_questions[2], "a"),
    Question(medium_world_questions[3], "c"),
    Question(medium_world_questions[4], "c"),
    Question(medium_world_questions[5], "c"),
]

medium_science_questions = [
    "Which of these options incorrectly pairs the ?\n(a) Caracas\n(b) Asunción\n(c) Quito\n(d) Montevideo",
    "Which of these cities is not in Turkey?\n(a) Gaziantep \n(b) Ankara \n(c) Istanbul \n(d) Patras",
    "How do you say “bye” in Portuguese?\n(a) tchau \n(b) adios \n(c) adieu \n(d) te vuelvas",
    "Which of these countries borders Thailand?\n(a) China\n(b) Vietnam \n(c) Cambodia \n(d) Singapore",
    "Something?\n(a) thing1\n(b) thing2",
    "himedu\n(a) thing1\n(b) thing2",
    "hdtdmedty\n(a) thing1\n(b) thing2"
]

medium_science_answers = [
    Question(medium_science_questions[0], "a"),
    Question(medium_science_questions[1], "d"),
    Question(medium_science_questions[2], "a"),
    Question(medium_science_questions[3], "c"),
    Question(medium_science_questions[4], "a"),
    Question(medium_science_questions[5], "a"),
    Question(medium_science_questions[6], "a"),
]

hard_world_questions = [
    "Which of these countries does not border Saudi Arabia?\n(a) Iraq \n(b) Iran\n (c) Kuwait\n (d) United Arab Emirates",
    "Which of these countries IS a member of NATO (North Atlantic Treaty Organization)?\n(a) Austria\n(b) Sweden\(c) Iceland\n(d) Finland",
    "How do you say “thank you” in Japanese?\n(a) ありがとう\n(b) さようなら\n(c) こんにちは\n(d) どういたしまして",
    "Which of these countries does not border Russia?\n(a) Lithuania\n(b) Latvia\n(c) Poland\n(d) Romania",
    "Which one of these capital cities is not located in Asia?\n(a) Dhaka\n(b) Khartoum\n(c) Jakarta\n(d) Tehran",
    "Of the following European countries, which is the largest by area?\n(a) Norway\n(b) Poland\n(c) Italy\n(d) Germany",

]

hard_world_answers = [
    Question(hard_world_questions[0], "b"),
    Question(hard_world_questions[1], "c"),
    Question(hard_world_questions[2], "a"),
    Question(hard_world_questions[3], "d"),
    Question(hard_world_questions[4], "b"),
    Question(hard_world_questions[5], "a"),
]

hard_science_questions = [
    "Which of these countries does not border Saudi Arabia?\n(a) Iraq \n(b) Iran\n (c) Kuwait\n (d) United Arab Emirates",
    "Which of these countries IS a member of NATO (North Atlantic Treaty Organization)?\n(a) Austria\n(b) Sweden\(c) Iceland\n(d) Finland",
    "How do you say “thank you” in Japanese?\n(a) ありがとう\n(b) さようなら\n(c) こんにちは\n(d) どういたしまして",
    "Which of these countries does not border Russia?\n(a) Lithuania\n(b) Latvia\n(c) Poland\n(d) Romania",
    "Which one of these capital cities is not located in Asia?\n(a) Dhaka\n(b) Khartoum\n(c) Jakarta\n(d) Tehran",
    "Of the following European countries, which is the largest by area?\n(a) Norway\n(b) Poland\n(c) Italy\n(d) Germany",

]

hard_science_answers = [
    Question(hard_science_questions[0], "b"),
    Question(hard_science_questions[1], "c"),
    Question(hard_science_questions[2], "a"),
    Question(hard_science_questions[3], "d"),
    Question(hard_science_questions[4], "b"),
    Question(hard_science_questions[5], "a"),
]

easy_topics = [easy_world_questions, easy_science_questions]
medium_topics = [medium_world_questions, medium_science_questions]
hard_topics = [hard_world_questions, hard_science_questions]

def time_funct():
    starttime = time.time()
    global player_answer
    player_answer = input(prompt)
    endtime = time.time()
    global elapsed
    elapsed = (endtime - starttime)

going = True

while rung_number > 0 and rung_number != 15:

    while rung_number >= 1 and rung_number <= 6 and going:
        for question in easy_world_answers or easy_science_answers:
            easy_question_type = random.choice(easy_topics)
            if easy_science_questions is None or easy_world_questions is None:
                rung_number = -1
                going = False
            elif easy_question_type == easy_world_questions:
                print("An EASY WORLD question has been SELECTED.")
                change_later = random.choice(easy_world_answers)
                prompt = change_later.prompt
                easy_world_answers.remove(change_later)
            elif easy_question_type == easy_science_questions:
                print("An EASY SCIENCE question has been SELECTED.")
                change_later = random.choice(easy_science_answers)
                prompt = change_later.prompt
                easy_science_answers.remove(change_later)

            time_funct()

            if elapsed > 10:
                print(f"You took too long (about {round(elapsed)} seconds)! You lost...")
                going = False
                rung_number = -1
            elif player_answer.lower() == change_later.answer:
                rung_number += 1
                print(f"CORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) > 0:
                rung_number -= fall_number
                print(f"INCORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) <= 0:
                rung_number -= fall_number
                print("INCORRECT. You lost the game...")
                rung_number = -1
                going = False
                break
            else:
                print("Not sure how you got here, but carry on...")

    while rung_number > 6 and rung_number <= 10 and going:
        for question in medium_world_answers or medium_science_answers:
            medium_question_type = random.choice(medium_topics)
            if medium_science_questions is None or medium_world_questions is None:
                rung_number = -1
                going = False
            elif medium_question_type == medium_world_questions:
                print("A MEDIUM WORLD question has been SELECTED.")
                change_later = random.choice(medium_world_answers)
                prompt = change_later.prompt
                medium_world_answers.remove(change_later)
            elif medium_question_type == medium_science_questions:
                print("A MEDIUM SCIENCE question has been SELECTED.")
                change_later = random.choice(medium_science_answers)
                prompt = change_later.prompt
                medium_science_answers.remove(change_later)

            time_funct()

            if elapsed > 10:
                print(f"You took too long (about {round(elapsed)} seconds)! You lost...")
                going = False
                rung_number = -1
            elif player_answer.lower() == change_later.answer:
                rung_number += 1
                print(f"CORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) > 0:
                rung_number -= fall_number
                print(f"INCORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) <= 0:
                rung_number -= fall_number
                print("INCORRECT. You lost the game...")
                rung_number = -1
                going = False
                break
            else:
                print("Not sure how you got here, but carry on...")

    while rung_number > 10 and rung_number < 15 and going:
        for question in hard_world_answers or hard_science_answers:
            hard_question_type = random.choice(hard_topics)
            if hard_science_questions is None or hard_world_questions is None:
                rung_number = -1
                going = False
            elif hard_question_type == hard_world_questions:
                print("A HARD WORLD question has been SELECTED.")
                change_later = random.choice(hard_world_answers)
                prompt = change_later.prompt
                hard_world_answers.remove(change_later)
            elif hard_question_type == hard_science_questions:
                print("A HARD SCIENCE question has been SELECTED.")
                change_later = random.choice(hard_science_answers)
                prompt = change_later.prompt
                hard_science_answers.remove(change_later)

            time_funct()

            if elapsed > 10:
                print(f"You took too long (about {round(elapsed)} seconds)! You lost...")
                going = False
                rung_number = -1
            elif player_answer.lower() == change_later.answer:
                rung_number += 1
                print(f"CORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) > 0:
                rung_number -= fall_number
                print(f"INCORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) <= 0:
                rung_number -= fall_number
                print("INCORRECT. You lost the game...")
                rung_number = -1
                going = False
                break
            else:
                print("Not sure how you got here, but carry on...")

if rung_number == 15:
    print("CONGRATULATIONS! You won the game!")

# remember to add your IF THERE ARE NO MORE QUESTIONS (if you fall 4 times you lose) function, SEPARATE CATEGORIES AND RANDOM SELECTION, BONUSES