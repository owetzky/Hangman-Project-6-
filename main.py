print("Welcome to the game of Hangman!")
print()

# store secrect word in a variable 
secretWord = "command"
guesses = []

# create a user input system, where they can only guess one letter at a time 
# create or use a function that will display the secret word, but only show the characters the user has guessed (the other characters should be _ underscores)
def getLetter():
  letter = ""
  
  while(len(letter) != 1):

    letter = input("Enter a Letter: ")
  return letter
    
  
def displaySecretWord(word, guesses):
 
# iterate through secret word
  for letter in word:
 
# if guessed letter is in secretWord, display the letter
    if(letter in guesses):
      print(letter, end=" ")
# if not => display an underscore ( _ )
    else:
      print("_", end=" ")


# function that determines if the user has won the game
def hasUserWon(word, guesses):
 
  # Let's use an "Innocent Until Proven Guilty" Algorithm...
  # ...and create a variable that is set to "True"
  won = True
 
  # Go through each letter in the secret word
  for letter in word:
 
    # Check if the letter has been guessed
    if(letter not in guesses):
 
      # If it has NOT been guessed, set the variable we created to False, and stop the loop
      won = False
      break
 
  return won

# create a dictionary to store the user's guesses
  # store the guess from the user 

# => main game loop <= 
secretWord = "command" 
strikes = 0
letter = ""
letters = []

# Take a guess from the user 
# create a variable that counts/holds how many guesses a user has (5 gueses max)
# display the correct or incorrect word results
while(not hasUserWon(secretWord, letters) and strikes != 5):
  letter = getLetter()
  letters.append(letter)
  displaySecretWord(secretWord, letters)
  
  if letter not in secretWord:
    strikes+=1
    print()
    print(f"Number of strikes: {strikes} out of 5")    


if (strikes == 5):
  print()
  print("Game over, you lost!")
  
else:
  print()
  print("Congratulations, you have won!")
  print(f"The secret word was '{secretWord}'!")

