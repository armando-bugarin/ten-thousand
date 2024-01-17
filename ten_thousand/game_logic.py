# ten_thousand/game_logic.py

import random  # Import the random module to generate random dice values
from collections import Counter

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
