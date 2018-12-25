import random
import time
import site
rung_number = 1
name = input("Welcome to Trivia Ladder! What's your name?")
print(f"Hello, {name}! The object of the game is to use your *worldly knowledge* to climb your way to the top! There are four basic categories: foreign languages, science, and geography. At each rung of the ladder, a category will be selected at random, and a multiple-choice question will be asked. Answer correctly, and you will move up one rung. Answer incorrectly, and you will move down on the ladder. Questions will become progressively more difficult. Make it all the way to Rung 15, and you win! Fall off the ladder, and you lose!")
mode = input("Would you like to play on EASY, MEDIUM, or HARD mode?")
valid_options = ["e".lower(), "easy".lower(), "m".lower(), "medium".lower(), "h".lower(), "hard".lower()]
while mode.lower() not in valid_options:
  mode = input("That was an invalid input. Choose from easy, medium, or hard.")
if mode.lower() == "e" or mode.lower() == "easy":
  fall_number = 2
elif mode.lower() == "m" or mode.lower() == "medium":
  fall_number = 5
elif mode.lower() == "h" or mode.lower() == "hard":
  fall_number = 10
print(f"You will fall {fall_number} rungs each time you answer incorrectly.")
ready_to_play = input("Are you ready to play?")
if ready_to_play.lower() == "yes" or ready_to_play.lower() == "y":
  print("Great! Let's begin...")
else:
  print("Oh well... We're still going to begin.")

easy_questions = {
  'easy_science': {
    'What is intracellular?': ['Desmosomes', 'Gap juncions', 'Plasmodesmata', 'Mitochondria'],
    'Whomst?' : ['Francis Crick', 'Rosalind', 'Watson', 'Parker'],
    'Where is zika virus?': ['Africa', 'USA', 'Portugal', 'Spain'],
    'What is cell?': ['Thing', 'Not thing', 'Wha', 'tf']
  },
  'easy_geography' : {
    'what is the biggest country?': ['Russia', 'China', 'South Korea', 'USA'],
    'where is wyoming?': ['Nowhere', 'USA', 'China', 'Korea'],
    'what is world?': ['Place', 'cell', 'pup', 'plant']
  },
  'easy_foreign_languages': {
    'what is hello in german?': ['hallo', 'ciao', 'czesc', 'merhaba'],
    'what is goodbye in turkish?': ['hoscakal', 'adios', 'ciao', 'bye']
  }
}

easy_questions_list = ["What is intracellular?", "Whomst?", "Where is zika virus", "What is cell?", "What even?", "Ok"]

medium_questions_list = ["What is the capital of Ohio?", "What is opposite the color red on the color wheel?", "tdtfdyt", "yhfy", "dty", "hiu", "ygyhguk", "re5rswerwer", "hdtdty"]

hard_questions_list = ["What is?", "Whomst?", "serser", "ygyugyug", "fyfuygui", "uhoiu", "ujhou", "esre", "tug", "ygg8o8u"]

while rung_number >= 1 and rung_number != 15:
  if rung_number >= 1 and rung_number < 6:
    question = random.choice(easy_questions_list)
    easy_questions_list.remove(question)
  if rung_number >= 6 and rung_number <= 10:
    question = random.choice(medium_questions_list)
    medium_questions_list.remove(question)
  if 10 < rung_number and rung_number <= 15:
    question = random.choice(hard_questions_list)
    hard_questions_list.remove(question)
    question = random.choice(hard_questions_list)
    hard_questions_list.remove(question)
  correct_answer = "yes"
  starttime = time.time()
  player_answer = input(question)
  endtime = time.time()
  if (endtime - starttime) > 15:
    print(f"You took too long ({(endtime - starttime)} seconds)! You lost the game...")
    break
  if player_answer == correct_answer:
    rung_number += 1
    print(f"CORRECT. You are now on Rung {rung_number}.")
  elif (rung_number - fall_number) > 0:
    rung_number -= fall_number
    print(f"INCORRECT. You are now on Rung {rung_number}.")
  elif (rung_number - fall_number) <= 0:
    rung_number -= fall_number
    print("You lost the game...")

if rung_number == 15:
  print("CONGRATULATIONS! You won the game!")
