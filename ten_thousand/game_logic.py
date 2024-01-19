# ten_thousand/game_logic.py

import random  # Import the random module to generate random dice values
from collections import Counter

# class Game:
    # def __init__(self):
    #     self.total_score = 0
    #     self.current_round = 1
    #     self.current_score = 0
    #     self.dice_to_set_aside = set()

    # def start_round(self):
    #     print(f"Starting Round {self.current_round}")
    #     self.dice_to_set_aside.clear()
    #     self.current_score = 0

    # def roll_dice(self, num_dice):
    #     dice_values = GameLogic.roll_dice(num_dice)
    #     print(f"Rolled dice: {dice_values}")
    #     return dice_values

    # def set_aside(self, dice_values):
    #     self.dice_to_set_aside.update(dice_values)
    #     print(f"Setting aside dice: {self.dice_to_set_aside}")

    # def calculate_score_and_bank(self):
    #     round_score = GameLogic.calculate_score(tuple(self.dice_to_set_aside))
    #     self.current_score += round_score
    #     self.total_score += self.current_score
    #     print(f"Current Round Score: {self.current_score}")
    #     print(f"Total Score: {self.total_score}")

    # def next_round_or_quit(self):
    #     choice = input("Do you want to (r)oll again, (b)ank the current score, or (q)uit? ").lower()
    #     if choice == 'r':
    #         self.current_round += 1
    #         return True
    #     elif choice == 'b':
    #         self.current_round += 1
    #         self.current_score = 0
    #         return True
    #     elif choice == 'q':
    #         print(f"Thanks for playing! Total Score: {self.total_score}")
    #         return False
    #     else:
    #         print("Invalid choice. Please enter 'r', 'b', or 'q'.")
    #         return True

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score for a given dice roll based on the rules of the game.
        Parameters:
        - dice_roll (tuple): A tuple of integers representing the values of the dice roll.
        Returns:
        - int: The calculated score for the dice roll.
        """
        score = 0
        # Use Counter to count occurrences of each number in the dice roll
        counts = Counter(dice_roll)
        # Check for a straight
        if len(dice_roll) == 6 and len(counts) == 6:
            return 1500
        # Check for three pairs
        if len(dice_roll) == 6 and all(count == 2 for count in counts.values()):
            return 1500
        for num, count in counts.items():
            if num == 1:
                if count >= 3:
                    score += 1000 + (count - 3) * 1000  # 1000 for three ones, plus 1000 for each additional one
                else:
                    score += count * 100  # Score for single ones
            elif num == 5:
                if count >= 3:
                    score += 500 + (count - 3) * 500  # 500 for three fives, plus 500 for each additional five
                else:
                    score += count * 50  # Score for single fives
            elif count >= 3:
                score += num * 100 + (count - 3) * num * 100  # 100 times the number for three of a kind, plus 100 times the number for each additional
        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        Simulate rolling a specified number of dice.

        Parameters:
        - num_dice (int): The number of dice to roll.

        Returns:
        - tuple: A tuple containing random values between 1 and 6, with length equal to num_dice.
        """
        # Use list comprehension to generate random values for each die
        dice_values = tuple(random.randint(1, 6) for _ in range(num_dice))
        return dice_values
