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
    "How do you say 'good morning' in Italian?\n(a) Buona notte\n(b) buenas noches\n(c) buongiorno\n(d)boa noite",
    "How do you say 'hunger' in Spanish?\n(a) hombre\n(b) hambre\n(c) hungre\n(d) humbre",
    "What is 'welcome' in French?\n(a) Bienvenue\n(b) Bienvenido\n(c) Bienvienue\n(d) Bienvena",
    "Which of these countries DOES NOT border Italy?\n(a) France\n(b) Austria\n(c) Slovenia\n(d) Germany",
    "Which of these countries is ?\n(a) thing1\n(b) thing2",
    "How do you say '' in ?\n(a) \n(b) \n(c) \n(d) ",
]

easy_world_answers = [
    Question(easy_world_questions[0], "a"),
    Question(easy_world_questions[1], "b"),
    Question(easy_world_questions[2], "a"),
    Question(easy_world_questions[3], "a"),
    Question(easy_world_questions[4], "a"),
    Question(easy_world_questions[5], "b"),
]

easy_science_questions = [
    "Which of these organelles is the powerhouse of the cell?\n(a) Golgi apparatus\n(b) Nucleus\n(c) Peroxisomes\n(d) Mitochondria",
    "Which of these macromolecules stores the most energy?\n(a) nucleic acids\n(b) lipids\n(c) carbohydrate\n(d) protein",
    "\n(a) thing1\n(b) thing2",
    "dtmedy\n(a) thing1\n(b) thing2",
    "himedu\n(a) thing1\n(b) thing2",
    "hdtdmedty\n(a) thing1\n(b) thing2",
]

easy_science_answers = [
    Question(easy_science_questions[0], "d"),
    Question(easy_science_questions[1], "b"),
    Question(easy_science_questions[2], "a"),
    Question(easy_science_questions[3], "a"),
    Question(easy_science_questions[4], "b"),
    Question(easy_science_questions[5], "a"),
]

medium_world_questions = [
    "What is the capital of Venezuela?\n(a) Caracas\n(b) Asunción\n(c) Quito\n(d) Montevideo",
    "Which of these cities is not in Turkey?\n(a) Gaziantep \n(b) Ankara \n(c) Istanbul \n(d) Patras",
    "How do you say “bye” in Portuguese?\n(a) tchau \n(b) adios \n(c) adieu \n(d) te vuelvas",
    "Which of these countries borders Thailand?\n(a) China\n(b) Vietnam \n(c) Cambodia \n(d) Singapore",
    "Which of these countries is NOT in Central America?\n(a) Belize\n(b) Costa Rica\n(c) Cuba\n(d) Guatemala",
    "Which of these countries is NOT located in Asia?\n(a) Sri Lanka\n(b) Bahrain\n(c) Algeria\n(d) Myanmar",
    "hdtdmedty\n(a) thing1\n(b) thing2,
]

medium_world_answers = [
    Question(medium_world_questions[0], "a"),
    Question(medium_world_questions[1], "b"),
    Question(medium_world_questions[2], "a"),
    Question(medium_world_questions[3], "a"),
    Question(medium_world_questions[4], "b"),
    Question(medium_world_questions[5], "a"),
]

medium_science_questions = [
    "What is the capital of Venezuela?\n(a) Caracas\n(b) Asunción\n(c) Quito\n(d) Montevideo",
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
hard_topics = [hard_world_questions, medium_science_questions]

while rung_number > 0 and rung_number != 15:

    while rung_number >= 1 and rung_number <= 6:
        for question in easy_world_questions or easy_science_questions:
            easy_question_type = random.choice(easy_topics)
            if easy_question_type == easy_world_questions:
                prompt = random.choice(easy_world_questions)
                easy_world_questions.remove(prompt)
            if easy_question_type == easy_science_questions:
                prompt = random.choice(easy_science_questions)
                easy_science_questions.remove(prompt)
            if not easy_science_questions or not easy_world_questions:
                print("You've fallen too many times...it seems as though the ladder is breaking!\nYou have lost.")

            starttime = time.time()
            player_answer = input(prompt)
            endtime = time.time()
            elapsed = (endtime - starttime)

            if elapsed > 10:
                print(f"You took too long (about {round(elapsed)} seconds)! You lost...")
                quit()
            if player_answer.lower() == question.answer:
                rung_number += 1
                print(f"CORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) > 0:
                rung_number -= fall_number
                print(f"INCORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) <= 0:
                rung_number -= fall_number
                print("INCORRECT. You lost the game...")
                quit()
            else:
                print("Not sure how you got here, but carry on...")

    while rung_number > 6 and rung_number <= 10:
        for question in medium_world_questions or medium_science_questions:
            medium_question_type = random.choice(medium_topics)
            if medium_question_type == medium_world_questions:
                prompt = random.choice(medium_world_questions)
                medium_world_questions.remove(prompt)
            if medium_question_type == medium_science_questions:
                prompt = random.choice(medium_science_questions)
                medium_science_questions.remove(prompt)
            if not medium_science_questions or not medium_world_questions:
                print("You've fallen too many times...it seems as though the ladder is breaking!\nYou have lost.")

            starttime = time.time()
            player_answer = input(prompt)
            endtime = time.time()
            elapsed = (endtime - starttime)

            if elapsed > 10:
                print(f"You took too long (about {round(elapsed)} seconds)! You have lost...")
                quit()
            if player_answer.lower() == question.answer:
                rung_number += 1
                print(f"CORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) > 0:
                rung_number -= fall_number
                print(f"INCORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) <= 0:
                rung_number -= fall_number
                print("INCORRECT. You lost the game...")
                quit()
            else:
                print("Not sure how you got here, but carry on...")

    while rung_number > 10 and rung_number < 15:
        for question in hard_world_questions or hard_science_questions:
            hard_question_type = random.choice(hard_topics)
            if hard_question_type == hard_world_questions:
                prompt = random.choice(hard_world_questions)
                hard_world_questions.remove(prompt)
            if hard_question_type == hard_science_questions:
                prompt = random.choice(hard_science_questions)
                hard_science_questions.remove(prompt)
            if not hard_science_questions or not hard_world_questions:
                print("You've fallen too many times...it seems as though the ladder is breaking!\nYou have lost.")

            starttime = time.time()
            player_answer = input(prompt)
            endtime = time.time()
            elapsed = (endtime - starttime)

            if elapsed > 10:
                print(f"You took too long (about {round(elapsed)} seconds)! You lost the game...")
                quit()
            if player_answer.lower() == question.answer:
                rung_number += 1
                print(f"CORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) > 0:
                rung_number -= fall_number
                print(f"INCORRECT. You are now on Rung {rung_number}.")
            elif (rung_number - fall_number) <= 0:
                rung_number -= fall_number
                print("INCORRECT. You lost the game...")
                quit()
            else:
                print("Not sure how you got here, but carry on...")

if rung_number == 15:
    print("CONGRATULATIONS! You won the game!")

# remember to add your IF THERE ARE NO MORE QUESTIONS (if you fall 4 times you lose) function, SEPARATE CATEGORIES AND RANDOM SELECTION, BONUSES