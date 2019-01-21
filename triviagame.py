# TRIVIA LADDER CODE

import random
import time # needed for random choices and time limit
rung_number = 1 # defining rung_number; user starts at the 1st rung

name = input("Welcome to Trivia Ladder! What's your name? ")
print(f"Hello, {name}! The object of the game is to use your *wordly knowledge* to climb your way to the top!\nThere are two basic categories: INTERNATIONAL and SCIENCE. At each rung of the ladder, a category will be selected at random, and a multiple-choice question will be asked.\nAnswer correctly, and you will move up one rung. Answer incorrectly, and you will move down on the ladder.\nQuestions will become progressively more difficult. You will have 15 SECONDS to answer each question.\nMake it all the way to Rung 15, and you win!\nFall off the ladder, and you lose!")
# explains rules to user
mode = input("Would you like to play on EASY, MEDIUM, or HARD mode? ")
valid_options = ["e", "easy", "m", "medium", "h", "hard"]
# user can choose from easy, medium, or hard mode

while mode.lower() not in valid_options: # account for typos with WHILE LOOP
    mode = input("That was an invalid input. Choose from easy, medium, or hard.")
# the harder the difficulty, the larger the fall when the user answers incorrectly
if mode.lower() == "e" or mode.lower() == "easy":
    fall_number = 2
elif mode.lower() == "m" or mode.lower() == "medium":
    fall_number = 4
elif mode.lower() == "h" or mode.lower() == "hard":
    fall_number = 7

print(f"You will fall {fall_number} rungs each time you answer incorrectly. ")
ready_to_play = input("Are you ready to play? ") # asks if user is ready

if ready_to_play.lower() == "yes" or ready_to_play.lower() == "y":
    print("Great! Let's begin...")
else:
    print("Oh well... We're still going to begin.")

"""
Creating the class Question, including a prompt and answer.
Will later be used to pair prompts to their correct answers with a dictionary.
"""
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# list of EASY INTERNATIONAL questions prompts and answer choices
easy_international_questions = [
    "How do you say 'good morning' in Italian?\n(a) Buona notte\n(b) Buenas noches\n(c) Buongiorno\n(d) Boa noite",
    "How do you say 'hunger' in Spanish?\n(a) Hombre\n(b) Hambre\n(c) Hungre\n(d) Humbre",
    "What is 'welcome' in French?\n(a) Bienvenue\n(b) Bienvenido\n(c) Bienvienue\n(d) Bienvena",
    "Which of these countries DOES NOT border Italy?\n(a) France\n(b) Austria\n(c) Switzerland\n(d) Germany",
    "Which of these places is NOT an actual country?\n(a) Bhutan\n(b) Wyoming\n(c) Burundi\n(d) Nauru",
    "Which of these places IS a country?\n(a) Greenland\n(b) Palestine\n(c) Vatican City\n(d) Wyoming",
    "What is Japan's currency?\n(a) Yuan\n(b) Yen\n(c) Dollar\n(d) Rupee",
    "Of the following languages, which is the most spoken?\n(a) Mandarin Chinese\n(b) Hindi\n(c) English\n(d) Russian",
]

# links each EASY INTERNATIONAL prompt to its correct answer with the Question class
easy_international_answers = [
    Question(easy_international_questions[0], "c"),
    Question(easy_international_questions[1], "b"),
    Question(easy_international_questions[2], "a"),
    Question(easy_international_questions[3], "d"),
    Question(easy_international_questions[4], "b"),
    Question(easy_international_questions[5], "c"),
    Question(easy_international_questions[6], "b"),
    Question(easy_international_questions[7], "a"),
]

# list of EASY SCIENCE questions prompts and answer choices
easy_science_questions = [
    "Which of these organelles is the powerhouse of the cell?\n(a) Golgi apparatus\n(b) Nucleus\n(c) Peroxisomes\n(d) Mitochondria",
    "Which of these macromolecules stores the most energy?\n(a) nucleic acids\n(b) lipids\n(c) carbohydrate\n(d) protein",
    "Which of these colors has the longest wavelength?\n(a) Red\n(b) Blue\n(c) Violet\n(d) Green",
    "What is the scientific name of E. Coli?\n(a) Escheria coli\n(b) Escherie coli\n(c) Echesheria coli\n(d) Escherichia coli",
    "Which of these is NOT a major type of rock?\n(a) Metamorphic\n(b) Igneous\n(c) Basalt\n(d) Sedimentary",
    "Which of these planets is closest to the Sun?\n(a) Mars\n(b) Earth\n(c) Venus\n(d) Mercury",
    "How does the Sun transfer energy to the Earth?\n(a) Conduction\n(b) Radiation\n(c) Convection\n(d) Reflection",
    "As the variable ______ increases, energy increases if all other variable are constant.\n(a) Wavelength\n(b) Distance\n(c) Frequency\n(d) Time",
    "Which of these layers of the atmosphere is farthest away?\n(a) Troposhere\n(b) Mesophere\n(c) Exosphere\n(d) Thermosphere",
]

# links each EASY SCIENCE prompt to its correct answer with the Question class
easy_science_answers = [
    Question(easy_science_questions[0], "d"),
    Question(easy_science_questions[1], "b"),
    Question(easy_science_questions[2], "a"),
    Question(easy_science_questions[3], "d"),
    Question(easy_science_questions[4], "c"),
    Question(easy_science_questions[5], "d"),
    Question(easy_science_questions[6], "b"),
    Question(easy_science_questions[7], "c"),
    Question(easy_science_questions[8], "c")
]

# list of MEDIUM INTERNATIONAL questions prompts and answer choices
medium_international_questions = [
    "What is the capital of Venezuela?\n(a) Caracas\n(b) Asunción\n(c) Quito\n(d) Montevideo",
    "Which of these cities is not in Turkey?\n(a) Gaziantep \n(b) Ankara \n(c) Istanbul \n(d) Patras",
    "How do you say “bye” in French?\n(a) Au revoir \n(b) Adios \n(c) Tchau \n(d) Te vuelvas",
    "Which of these countries borders China?\n(a) Japan\n(b) South Korea \n(c) India \n(d) Singapore",
    "Which of these countries is NOT in Central America?\n(a) Belize\n(b) Costa Rica\n(c) Cuba\n(d) Guatemala",
    "Which of these countries is NOT located in Asia?\n(a) Sri Lanka\n(b) Bahrain\n(c) Algeria\n(d) Myanmar",
    "Which of these is NOT a Romance language?\n(a) French\n(b) Portuguese\n(c) German\n(d) Italian",
    "Which of these countries is not on the same continent as the other three?\n(a) Somalia\n(b) Saudi Arabia\n(c) Angola\n(d) Sudan",
    "What is the second largest continent by area?\n(a) Africa\n(b) Latin America\n(c) North America\n(d) Europe",
]

# links each MEDIUM INTERNATIONAL prompt to its correct answer with the Question class
medium_international_answers = [
    Question(medium_international_questions[0], "a"),
    Question(medium_international_questions[1], "d"),
    Question(medium_international_questions[2], "a"),
    Question(medium_international_questions[3], "c"),
    Question(medium_international_questions[4], "c"),
    Question(medium_international_questions[5], "c"),
    Question(medium_international_questions[6], "c"),
    Question(medium_international_questions[7], "b"),
    Question(medium_international_questions[8], "a"),
]

# list of MEDIUM SCIENCE questions prompts and answer choices
medium_science_questions = [
    "Which of these processes is an example of an endothermic reaction?\n(a) Ice melting\n(b) Combustion\n(c) Neutralization\n(d) Rusting",
    "The normal force (N) is directed _______ to two surfaces in contact.\n(a) Parallel\n(b) Adjacent \n(c) Tangent \n(d) Perpendicular",
    "Which of these elements has the highest molar mass?\n(a) Iron \n(b) Nickel \n(c) Lead \n(d) Bismuth",
    "As pressure increases, which of these variables decreases if the rest are held constant?\n(a) Temperature\n(b) Rate \n(c) Volume \n(d) Moles",
    "As the source of sound and an observer move farther away, the sound's observed frequency _______.\n(a) Increases\n(b) Stays the same\n(c) Decreases\n(d) Approaches infinity",
    "Chemical equilibrium occurs when the ______ of the forward reaction equal(s) that of the backward reaction.\n(a) Rate\n(b) Energy\n(c) Concentration\n(d) Reactant mass",
    "Which of the following is the smallest in size?\n(a) Virus\n(b) Cell\n(c) Bacterium\n(d) Archaea"
]

# links each MEDIUM SCIENCE prompt to its correct answer with the Question class
medium_science_answers = [
    Question(medium_science_questions[0], "a"),
    Question(medium_science_questions[1], "d"),
    Question(medium_science_questions[2], "d"),
    Question(medium_science_questions[3], "c"),
    Question(medium_science_questions[4], "c"),
    Question(medium_science_questions[5], "a"),
    Question(medium_science_questions[6], "a"),
]

# list of HARD INTERNATIONAL questions prompts and answer choices
hard_international_questions = [
    "Which of these countries does not border Saudi Arabia?\n(a) Iraq \n(b) Iran\n(c) Kuwait\n(d) United Arab Emirates",
    "Which of these countries IS NOT a member of NATO (North Atlantic Treaty Organization)?\n(a) Turkey\n(b) Greece\n(c) Sweden\n(d) Canada",
    "How do you say “thank you” in Japanese?\n(a) ありがとう\n(b) さようなら\n(c) こんにちは\n(d) どういたしまして",
    "Which of these countries does not border Russia?\n(a) Norway\n(b) Finland\n(c) Poland\n(d) Romania",
    "Which one of these capital cities is not located in Asia?\n(a) Manila\n(b) Khartoum\n(c) Jakarta\n(d) Tehran",
    "Of the following European countries, which is the smallest by area?\n(a) Liechtenstein\n(b) Poland\n(c) Italy\n(d) Germany",

]

# links each HARD INTERNATIONAL prompt to its correct answer with the Question class
hard_international_answers = [
    Question(hard_international_questions[0], "b"),
    Question(hard_international_questions[1], "c"),
    Question(hard_international_questions[2], "a"),
    Question(hard_international_questions[3], "d"),
    Question(hard_international_questions[4], "b"),
    Question(hard_international_questions[5], "a"),
]

# list of HARD SCIENCE questions prompts and answer choices
hard_science_questions = [
    "Sound travels the fastest through which state of matter?\n(a) Liquids \n(b) Solids\n(c) Plasma\n(d) Gases",
    "Which of these options is not a type of a protein filament?\n(a) Intermediate filament\n(b) Microtubule\n(c) Microactin \n(d) Microfilament",
    "For an aircraft to rise, which of these forces must meet or exceed the force of gravity?\n(a) Drag\n(b) Thrust\n(c) Lift\n(d) Weight",
    "The speed of light is slowest in which medium?\n(a) Solid\n(b) Vacuum\n(c) Air\n(d) Liquid",
    "What is the cancer of a connective tissue called?\n(a) Glioblastoma\n(b) Carcinoma\n(c) Melanoma\n(d) Sarcoma",
    "A reaction will occur spontaneously if _______ is less than 0.\n(a) Entropy\n(b) Enthalpy\n(c) Gibbs free energy\n(d) Temperature",
]

# links each HARD SCIENCE prompt to its correct answer with the Question class
hard_science_answers = [
    Question(hard_science_questions[0], "b"),
    Question(hard_science_questions[1], "c"),
    Question(hard_science_questions[2], "c"),
    Question(hard_science_questions[3], "a"),
    Question(hard_science_questions[4], "d"),
    Question(hard_science_questions[5], "c"),
]

# list of special EAGLE questions
eagle_questions = [
    "Thanks to your kind, what is the most polluted city in the US by ozone? Think carefully...\n(a) Miami\n(b) Los Angeles\n(c) New York\n(d) San Diego",
    "Which state is home to the most national parks? Choose wisely...\n(a) California\n(b) Alaska\n(c) New Jersey\n(d) Colorado",
    "What was the first national park created in the US? Be careful... CAW!\n(a) Rocky Mountain\n(b) Hot Springs\n(c) Yosemite\n(d) Yellowstone",
    "Which country has the cleanest air in the world? Think carefully...\n(a) Denmark\n(b) USA\n(c) Finland\n(d) France",
]

# links special EAGLE prompt to its correct answer with Question class
eagle_answers = [
    Question(eagle_questions[0], "b"),
    Question(eagle_questions[1], "a"),
    Question(eagle_questions[2], "d"),
    Question(eagle_questions[3], "c"),
]

# list of EASY, MEDIUM, and HARD topics used to randomly pick a topic in each difficulty level
easy_topics = [easy_international_questions, easy_science_questions]
medium_topics = [medium_international_questions, medium_science_questions]
hard_topics = [hard_international_questions, hard_science_questions]

"""
rung_funct() asks the user a question, times how long the user takes to answer, and evaluates the response.
"""
def rung_funct():
    starttime = time.time() # starts timer
    global player_answer # globalizing variables for use in the FOR and WHILE loops
    global elapsed
    global rung_number
    global fall_number
    global prompt
    global question_pair
    global game_in_play

# used as a fun way to ensure User does not run into an error if the question list is empty.
    if rung_number <= 0: # this is only true when the user has run out of questions because it is at the start of the function, before a question is asked.
        print("Woah! A mysterious EAGLE has taken you off the ladder and carried you to its nest near the top of the ladder.\nBefore it decides to devour you or return you, the eagle has one final question...")
        print("Caw, caw! I, the great EAGLE of the EAST, run these forests! I'm tired of these city slickers polluting my forests with their LADDERS... If you can get this next nature question right, I might spare you...")
        question_pair = random.choice(eagle_answers) # randomly selects a question pair from the special eagle_list
        prompt = question_pair.prompt # defines prompt
        player_answer = input(f"{prompt}\n") # asks user the question prompt
        if player_answer.lower() == question_pair.answer: # happens when user types correct response
            print("CORRECT. The mysterious EAGLE has returned you to the top of the ladder! You have WON the game!") # user has won.
        else:
            print("INCORRECT. The mysterious EAGLE has decided to keep you as its next meal... You have LOST the game!")
    else:
        player_answer = input(f"{prompt}\n") # asks user the question prompt
        endtime = time.time() # ends timer when he/she responds
        elapsed = (endtime - starttime) # calculates how long it took to answer

        if elapsed > 15:
            print(f"You took too long (about {round(elapsed)} seconds)! You lost...")
            game_in_play = False
            rung_number = -1 # player loses if he/she takes too long
        elif player_answer.lower() == question_pair.answer: # happens when user types correct response
            rung_number += 1
            print(f"CORRECT. You are now on Rung {rung_number}.")
        elif (rung_number - fall_number) > 0: # happens when User is incorrect but is not low enough to lose.
            rung_number -= fall_number
            print(f"INCORRECT. You are now on Rung {rung_number}.")
        elif (rung_number - fall_number) <= 0: # happens when User is incorrect and low enough to lose.
            rung_number -= fall_number
            print("INCORRECT. You lost the game...")
            rung_number = -100
            game_in_play = False
        else:
            print("Not sure how you got here, but carry on...") # just in case there was an option that was unaccounted for.

game_in_play = True # back-up in case setting rung_number negative when the player is supposed to lose does not work.

while rung_number > 0 and rung_number < 20 and game_in_play == True: # User has not won or lost yet if this is running

    for question in easy_international_answers or easy_science_answers:
        while rung_number >= 1 and rung_number <= 6 and game_in_play == True: # User is asked EASY questions
            easy_question_type = random.choice(easy_topics) # TOPIC is randomly selected. Can be INTERNATIONAL or SCIENCE questions.
            if len(easy_international_answers) == 0 or len(easy_science_answers) == 0: # if User is out of EASY questions, he/she will lose when rung_funct() runs because rung_funct() asks if rung_number <= 0
                rung_number = -100
                game_in_play = False # back-up in case setting rung_number to a negative number does not work
            elif easy_question_type == easy_international_questions: # if EASY INTERNATIONAL was picked
                print("An EASY INTERNATIONAL question has been SELECTED.")
                question_pair = random.choice(easy_international_answers) # randomly selects a question pair from the chosen TOPIC
                prompt = question_pair.prompt # defines prompt
                easy_international_answers.remove(question_pair) # ensures that questions are not repeated
            elif easy_question_type == easy_science_questions: # if EASY SCIENCE was picked
                print("An EASY SCIENCE question has been SELECTED.")
                question_pair = random.choice(easy_science_answers) # randomly selects a question pair from the chosen TOPIC
                prompt = question_pair.prompt # defines prompt
                easy_science_answers.remove(question_pair) # ensures questions are not repeated
            rung_funct() # runs rung_funct() * see above for the function

# All of the same comments for EASY QUESTIONS apply. In this block of code, MEDIUM level questions are asked.
    for question in medium_international_answers or medium_science_answers:
        while rung_number >= 7 and rung_number <= 14 and game_in_play == True:
            medium_question_type = random.choice(medium_topics)
            if len(medium_international_answers) == 0 or len(medium_science_answers) == 0:
                rung_number = -100
                game_in_play = False
            elif medium_science_answers is None or medium_international_answers is None:
                rung_number = -100
                game_in_play = False
            elif medium_question_type == medium_international_questions:
                print("A MEDIUM INTERNATIONAL question has been SELECTED.")
                question_pair = random.choice(medium_international_answers)
                prompt = question_pair.prompt
                medium_international_answers.remove(question_pair)
            elif medium_question_type == medium_science_questions:
                print("A MEDIUM SCIENCE question has been SELECTED.")
                question_pair = random.choice(medium_science_answers)
                prompt = question_pair.prompt
                medium_science_answers.remove(question_pair)
            rung_funct()

# All of the same comments for EASY QUESTIONS apply. In this block of code, HARD level questions are asked.
    for question in hard_international_answers or hard_science_answers:
        while rung_number > 14 and rung_number < 20 and game_in_play == True:
            hard_question_type = random.choice(hard_topics)
            if len(hard_international_answers) == 0 or len(hard_science_answers) == 0:
                rung_number = -100
                game_in_play = False
            elif hard_science_answers is None or hard_international_answers is None:
                rung_number = -100
                game_in_play = False
            elif hard_question_type == hard_international_questions:
                print("A HARD INTERNATIONAL question has been SELECTED.")
                question_pair = random.choice(hard_international_answers)
                prompt = question_pair.prompt
                hard_international_answers.remove(question_pair)
            elif hard_question_type == hard_science_questions:
                print("A HARD SCIENCE question has been SELECTED.")
                question_pair = random.choice(hard_science_answers)
                prompt = question_pair.prompt
                hard_science_answers.remove(question_pair)
            rung_funct()

if rung_number == 20: # exits WHILE loop when the user climbs to Rung 20. User wins game.
    print("CONGRATULATIONS! You have won TRIVIA LADDER!")