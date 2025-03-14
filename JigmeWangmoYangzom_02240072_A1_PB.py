def game_menu():
    x = input("Do you want to enter the Game World (yes or no):")
    if x.lower() == "yes":
         print("Welcome to Game World")
         print("Two games:")
         print("1. Mystery Digit: guess the number")
         print("2. Rock Paper Scissor")
         print("3. Exit")
    game_choice= int(input("Select game:"))          #allows to player to chose the game
    return game_choice
game_choice = game_menu()
     
def Mystery_Digit():
    import random           # imports random nubers to be guessed in the game

    lower_limit = 2         # the hidden_number will be between 2 and 99
    upper_limit = 99

    hidden_number = random.randint(lower_limit, upper_limit)    # random.randint function is to make random integer between the limits.

    print(f"Welcome to the Mystery Digit Game!")               

    print("Game Guide Lines")
    print("1. It is a game where you guess a number")
    print("2. You can guess a numeber between 2 to 99")
    print("3. If your guess is correct you win the game ")
    print("4. You get to try for 5 times")
    


    attempts = 0                       # starting attempts from 0
    max_attempts = 5                   # maximum number of attempts a player can used 

    while attempts < max_attempts:                   # Loop for the game, giving the player multiple attempts
        guess = int(input("Enter your guess: "))
        if guess < lower_limit or guess > upper_limit:
            print(f"Please enter a number between {lower_limit} and {upper_limit}.")
            continue
        
        attempts += 1   # Increase the attempt count by 1
        
        if guess == hidden_number:
            print(f"Congratulations! you have found the mystery number in {attempts} attempts!")
            break
        elif guess < hidden_number:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")

    if attempts == max_attempts and guess != hidden_number:                           
        print(f"Oops! GAME OVER!. The Mystery Number was {hidden_number}. Better luck next time!")
    

def Rock_Paper_Scissor():
    choices_available = ["rock", "paper", "scissor"]           # the choices available for the game
    import random                                               # import function from the above choices_avialable
    
    x = input("Your choice(rock or paper or scissor):")          
    y = random.choice(choices_available)                        # random.choice function to make the computer choose randomly from the choices available
    print("The Computer's choice:",y)
    if x == y or y == x:
        print("Draw")
    elif (x == "rock" and y == "paper") or (x == "scissor" and y == "rock") or (x == "paper" and y == "scissor"):
        print("You lose")
    else:
        print("you won!")

def Exit():
    u = input("Do yo really want to EXIT(yes or no):")
    if u == "no":
        game_menu()                 # if the player does not want to exit then the game menu will be displayed and the player can choose a game to play again
    else:
        print("Goodbye")
        
      
while True:
    if game_choice == 3:
         Exit()                     # will take the player to the Exit function
         break                      # if the player chooses 3 then they can exit the game and break the loop
    elif game_choice == 1:
        Mystery_Digit()             # if the player chooses 1 then they can play the Mystery Digit game
    elif game_choice == 2:          
        Rock_Paper_Scissor()        # if the player chooses 2 then they can play the Rock Paper Scissor game

    z = input("do you want to play again (yes or no):")
    if z.lower() == "no":
        Exit()
        break 
    else:                      # To exit loop
        game_choice = game_menu()     # if the player chooses yes then the game menu will be displayed 
        
    
    
        

