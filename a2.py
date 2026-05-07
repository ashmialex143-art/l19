import random
while True:
    ua = input("enter a choice (rock,paper,scissor):")
    possible_action = ["rock","paper","scissor"]
    ca = random.choice(possible_action)
    print(f"\n you chose {ua},computer chose{ca}.\n ")
    if ua == ca:
        print("it's a tie!")
    elif ua == "rock":
        if ca == "scissor":
            print("user win!")
        else:
            print("computer wins")
    elif ua == "paper":
        if ca == "rock":
            print("user win!")
        else:
            print("computer wins")
    elif ua == "scissor":
        if ca == "paper":
            print("user win!")
        else:
            print("computer wins")
    play_again = input("play again?(y/n):")
    if play_again != "y":
        break
    