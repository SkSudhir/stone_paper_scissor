import random

rounds = 10
comp_won = 0
user_won = 0
while rounds > 0:
    game_input = ["Stone", "Paper", "Scissor"]
    comp_input = random.choice(game_input)
    # print(comp_input)

    user_input = input("Choose:\n1. Stone\n2. Paper\n3. Scissor\n")
    user_input.capitalize()

    if comp_input == user_input:
        print(comp_input)
        print("Same choice, cancelled")
        rounds -= 1
        print("Rounds left: ", rounds)
        print("Scores: ", comp_won, " - ", user_won)
    elif comp_input == "Stone" and user_input == "Paper":
        print(comp_input)
        print("You won this round")
        user_won = user_won + 1
        rounds -= 1
        print("Rounds left: ", rounds)
        print("Scores: ", comp_won, " - ", user_won)
    elif comp_input == "Stone" and user_input == "Scissor":
        print(comp_input)
        print("I won this round")
        comp_won = comp_won + 1
        rounds -= 1
        print("Rounds left: ", rounds)
        print("Scores: ", comp_won, " - ", user_won)
    elif comp_input == "Paper" and user_input == "Stone":
        print(comp_input)
        print("I won this round")
        comp_won += 1
        rounds -= 1
        print("Rounds left: ", rounds)
        print("Scores: ", comp_won, " - ", user_won)
    elif comp_input == "Paper" and user_input == "Scissor":
        print(comp_input)
        print("You won this round")
        user_won += 1
        rounds -= 1
        print("Rounds left: ", rounds)
        print("Scores: ", comp_won, " - ", user_won)
    elif comp_input == "Scissor" and user_input == "Paper":
        print(comp_input)
        print("I won this round")
        comp_won += 1
        rounds -= 1
        print("Rounds left: ", rounds)
        print("Scores: ", comp_won, " - ", user_won)
    elif comp_input == "Scissor" and user_input == "Stone":
        print(comp_input)
        print("You won this round")
        user_won += 1
        rounds -= 1
        print("Rounds left: ", rounds)
        print("Scores: ", comp_won, " - ", user_won)
    else:
        print("Wrong Input")
else:
    if user_won > comp_won:
        print("Game over and the winner is Sudhir")
    elif user_won == comp_won:
        print("It's a tie, enjoy")
    else:
        print("Game over and the winner is Computer")
