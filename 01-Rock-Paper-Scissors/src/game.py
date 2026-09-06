""" 
Author: Soheila Abbasi
Date Created: 06/09/2026
Description: Rock Paper Scissors game.
"""


import random
from typing import List, Tuple


class RockPaperScissors:
    """ A simple Rock-Paper-Scissors game where a player can play against the computer."""
    def __init__(self, name: str):
        self.choices = ["rock", "paper", "scissors"]
        self.player_name = name

    def get_player_choice(self):
        user_choice = input(f"Enter your choice ({self.choices}): ")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        else:
            print(f"Invalid choice, you must select from {self.choices}.")
            return self.get_player_choice()

    """ Get the computer's choice randomly from the available choices."""
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice, computer_choice):
        """ Decide the winner based on the rules of Rock-Paper-Scissors.
        :param user_choice: The choice made by the player.
        :param computer_choice: The choice made by the computer.
        :return: A string indicating the result of the game.
        """
        if user_choice == computer_choice:
            return "It's a   Tie!"
            
        elif (user_choice, computer_choice) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
            return f"{self.player_name} won!"
        else:
            return "Computer won!"

        
    def play(self):
        """ Play the game.
          - Get the player's choice.
          - Get the computer's choice.
          - Decide the winner 
          - print the result.
          """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(self.decide_winner(user_choice, computer_choice))
        print(f'User choice: {user_choice}, Computer choice: {computer_choice}')
        

if __name__ == "__main__":  
    game = RockPaperScissors("Soli")

    while True:
        game.play()

        continue_game = input("Do you want to play again? (Enter any key to play again, enter q/Q to quit)")
        if continue_game.lower() == 'q':
            print("Thanks for playing!")
            break

