import random
print("Welcome to Rock Paper Scissors!")
while True:
    playOfHuman = input("Enter your play: ")
    compChoices = ["rock", "paper", "scissors"]
    playOfComp = random.choice(compChoices)
    if playOfHuman == "R" or playOfHuman == "r":
        playOfHuman = "rock"
    elif playOfHuman == "P" or playOfHuman == "p":
        playOfHuman = "paper"
    elif playOfHuman == "S" or playOfHuman == "s":
        playOfHuman = "scissors"
    print(f"You played {playOfHuman} and the computer played {playOfComp}.")
    if playOfHuman == playOfComp:
        print(f"Tie!")
    elif playOfHuman == "rock":
        if playOfComp == "paper":
            print(f"Paper covers rock. The computer wins!")
        else:
            print("Rock smashes scissors. You win!")
    elif playOfHuman == "paper": 
        if playOfComp == "rock":
            print(f"Paper covers rock. You win!")
        else:
            print("Scissors cut paper. The computer wins!")
    elif playOfHuman == "scissors": 
        if playOfComp == "rock":
            print(f"Rock smashes scissors. The computer wins!")
        else:
            print("Scissors cut paper. You win!")

    playAgain = input("Play again?(y/n)")
    if playAgain == "n":
        break