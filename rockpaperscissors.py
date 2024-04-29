import random
from enum import IntEnum

class Action(IntEnum):
    rock = 0
    paper = 1
    scissors = 2

def get_user_action():
    possible_actions = ", ".join([f"{action.value} for {action.name}" for action in Action])
    try:
        action = int(input(f"Choose an action ({possible_actions}): "))
        if action in Action._value2member_map_:
            return action
    except ValueError as e:
        print(f"\nInvalid action. Please, choose an option in range [0 to {len(Action) - 1}].\n")
        return get_user_action()

def get_computer_action():
    return Action(random.randint(0, len(Action) - 1))

def get_action_name(action):
    return Action(action).name

def determine_winner(user_action, computer_action):
    # first value = user action, second value = computer action
    outcomes = {
        (Action.rock, Action.scissors): "Rock smashes scissors, you win!",
        (Action.scissors, Action.rock): "Rock smashes scissors, you lose!",
        (Action.paper, Action.rock): "Paper covers rock, you win!",
        (Action.rock, Action.paper): "Paper covers rock, you lose!",
        (Action.scissors, Action.paper): "Scissors cuts paper, you win!",
        (Action.paper, Action.scissors): "Scissors cuts paper, you lose!"
    }

    if (user_action == computer_action):
        return f"Both players chose {get_action_name(user_action)}. It's a tie!"
    else:
        return outcomes.get((user_action, computer_action), "Invalid actions.")

if __name__ == "__main__":
    while True:
        user_action = get_user_action()
        computer_action = get_computer_action()

        print(f"\nYou: {get_action_name(user_action)}\nComputer: {get_action_name(computer_action)}")

        print(f"\n{determine_winner(user_action, computer_action)}")

        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() == "y":
            print("")
        else:
            break