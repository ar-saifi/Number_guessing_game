import random
def startGame():
  global computerNumber
  computerNumber=random.randrange(1,101)   #101 is not included
  print(computerNumber)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  print('''Please select the difficulty level:
  1. Easy(10 chances)
  2. Medium (5 chances)
  3. Hard (3 chances)
  ''')
  choice=input("Enter your choice:\n'easy'\n'medium'\n'hard'\n")
  if choice=='easy':
    print(f"Great! You have selected the {choice} difficulty level.\nLet's start the game!\n")
    game(10)
  elif choice=='medium':
    print(f"Great! You have selected the {choice} difficulty level.\nLet's start the game!\n")
    game(5)
  elif choice=='hard':
    print(f"Great! You have selected the {choice} difficulty level.\nLet's start the game!\n")
    game(3)
  else:
    print("enter from given levels.")
    startGame()

def hints():
  print(f"Number is between {computerNumber-(random.randrange(0,10))} and {computerNumber+(random.randrange(0,10))}")
  

def game(attempts):
  done=0
  total_hint=0
  while done < attempts:
    done+=1
    userGuess=int(input("Enter your guess:\n"))
    if userGuess==computerNumber:
      print(f"Congratulations! you guessed the correct number in {done} attempts using {total_hint} hints. ")
      playAgain=int(input("Wants to play again. \n Yes: press 1 \n No: press 2\n"))
      if playAgain==1:
        print("Let's play")
        startGame()
      else:
        break
    elif userGuess>computerNumber:
      print(f"Incorrect! The number is less than {userGuess}.")
      wantHint=int(input("Do you want hint ? \n Yes: press 1 \n No: press 2\n "))
      if wantHint==1:
        total_hint+=1
        hints()
    elif userGuess<computerNumber:
      print(f"Incorrect! The number is greater than {userGuess}.")
      wantHint=int(input("Do you want hint ? \n Yes: press 1 \n No: press 2\n "))
      if wantHint==1:
        total_hint+=1
        hints()
    if done==attempts and userGuess!=computerNumber:
      playAgain=int(input("Wants to play again. \n Yes: press 1 \n No: press 2\n"))
      if playAgain==1:
        print("Let's play")
        startGame()
      else:
        break



startGame()