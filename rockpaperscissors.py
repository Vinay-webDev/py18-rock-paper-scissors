#ROCK,PAPER,SCISSORS!!!!!!
import random
while 1==1:
    list = ["rock","paper","scissors"]
    computer = random.choice(list)
    player = None    # None means nothing or no value holds no value ********
    while player not in list:
        player = input("rock, paper, or scissors?: ").lower()
    print("computer: ",computer)
    print("player: ",player)
    if computer == player:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose!")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you win!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("you win!")
    play_again = input("wanna play again? (yes/no): ")
    if play_again != "yes":
        break
print("bye!")
