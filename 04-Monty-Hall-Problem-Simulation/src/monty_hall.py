import random
from typing import Tuple


# Function returns True or False
def monty_hall_game(switch_doors: bool) -> bool:
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
    door_revealed = random.choice(doors_revealed)

    # we get the 'switch_doors' from input of the function:
    # True: if player wants to switch from his initial choice
    # False: if player doesn't want to switch from his initial choice
    if switch_doors:
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'


def simulate_game(num_games: int) -> Tuple[float, float]:
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(num_games)])
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(num_games)])
    
    return num_wins_without_switching / num_games, num_wins_with_switching / num_games

# returm percentage by dividing to the num_games


if __name__ == '__main__':
    num_games = 1000
    win_percent_without_switching, win_percent_with_switching = simulate_game(num_games)
