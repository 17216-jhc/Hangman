#Source: https://www.youtube.com/watch?v=5x6iAKdJB6U
import random

#----FUNCTIONS------
def clear():
   print("\033[H\033[J", end="")

def input_checker(guess):
   #testing if a letter is inputted
  if guess.isalpha() == True:
    print()
  else:
    print("Sorry, please type in a letter")

  #testing if there is only one letter inputted
  if len(guess) == 1:
    print()
  else:
    print("Sorry, please type in only one letter")
    print()
    guess = input(f"Allowed guesses Left {allowed_guesses}, Next Guess: ")
    guesses.append(guess.lower())
    print()

def print_alphabet():
    for i in range(0,2):
        for j in range(0,14):
            print (map[i][j], end="")
            if j != 0:
                print ("|", end="")
        print ("")
  
#-----MAIN ROUTINE -----
with open('wordlist.txt', 'r') as f:
  words = f.readlines()

word = random.choice(words)[:-1]


  
allowed_guesses = 9
guesses = []
done = False

map= [["|", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K" , "L", "M"],
      ["|", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X" , "Y", "Z"]]

#make it only accept letters, 
while not done:
  #clear()
  print_alphabet()
  for letter in word:
    if letter.lower() in guesses:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print("")

  guess = input(f"Allowed guesses Left {allowed_guesses}, Next Guess: ")
  guesses.append(guess.lower())  

  input_checker(guess)

  if guess.lower() not in word.lower():
    allowed_guesses -= 1
    if allowed_guesses == 0:
      break
      
  done = True
  for letter in word:
    if letter.lower() not in guesses:
      done = False

if done:
  print(f"You found the word! it was {word}! You had {allowed_guesses} guesses left")
else:
  print(f"Game Over! The word was {word}!")