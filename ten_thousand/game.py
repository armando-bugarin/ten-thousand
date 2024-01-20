from ten_thousand.game_logic import GameLogic
import sys

# need to import GameLogic from game_logic.py?
# dice_roller = GameLogic.roll_dice -- need for lab 8?
# can put functions for rolling dice game in play function

num_rounds = 5

current_round = 1

total_score = 0
current_round = 1
current_score = 0
num_rounds = 5
dice_to_set_aside = set()

def play(roller=None): # changed from main to play to match test_sim_basic.py

    invite_to_play()

    start_game()

    while True:
        start_round(num_rounds) # has argument; real deal variable

        # num_dice = input("Enter the number of dice to roll:")
        # print(num_dice)
        # dice_values = roll_dice(num_dice)

        choice = input("Do you want to set aside dice? (y/n): ").lower()
        if choice == 'y':
            dice_to_set_aside = tuple(map(int, input("Enter the dice values to set aside (space-separated): ").split()))
            set_aside(dice_to_set_aside)

        calculate_score_and_bank()

        if not next_round_or_quit():
            break


def invite_to_play():
     print("Welcome to Ten Thousand")
     print("(y)es to play or (n)o to decline")
    #  play()
     choice = input("> ").lower()
     if choice == 'n':
         print("OK. Maybe another time")
         sys.exit() # short for system, will stop file
        #  exit()
     elif choice == 'y':
         return True
     else:
         print("Invalid choice. Please enter 'y' or 'n'.")
         return invite_to_play()
    #  play()
     

def start_game():
     global num_rounds
     print("Starting round 1")
     print("Rolling 6 dice...")

     num_dice = 6
     dice_values = roll_dice(num_dice)
     
     print("Enter dice to keep, or (q)uit:")
     choice = input("> ").lower()
     if choice == 'q':
          print("Thanks for playing. You earned 0 points")
          sys.exit()


def start_round(number_rounds): # parameter name should never be same as real variable name. but it can be similar
        if current_round < number_rounds:
            print(f"Starting Round {current_round}")
            dice_to_set_aside.clear()
            current_score = 0
        else:
                print("Thanks for playing! Total Score: {total_score}")
                return False
        

def do_round(current_round):
    print(f"Starting Round {current_round}")
    dice_to_set_aside.clear()
    current_score = 0
        

def roll_dice(num_dice):
        dice_values = GameLogic.roll_dice(num_dice)
        print(f"Rolled dice: {dice_values}")
        return dice_values


def dice_to_roll(dice_values, dice_to_set_aside):
    dice_to_roll = len(dice_values) - len(dice_to_set_aside)
    return dice_to_roll
     

# determine the num_dice for the next roll. dice_to_roll = len(dice_values-)- len(dice_to_set_aside).
def set_aside(dice_values):
        dice_to_set_aside.update(dice_values)
        print(f"Setting aside dice: {dice_to_set_aside}")


def num_dice_to_roll(dice_values, dice_to_set_aside):
    num_dice_to_roll = len(dice_values) - len(dice_to_set_aside)
    return num_dice_to_roll


def calculate_score_and_bank():
        global current_score
        round_score = GameLogic.calculate_score(tuple(dice_to_set_aside))
        current_score += round_score
        global total_score
        total_score += current_score
        print(f"Current Round Score: {current_score}")
        print(f"Total Score: {total_score}")


def next_round_or_quit():
        global current_round
        global current_score
        global total_score
        choice = input("Do you want to (r)oll again, (b)ank the current score, or (q)uit? ").lower()
        if choice == 'r':
            current_round += 1
            return True
        elif choice == 'b':
            current_round += 1
            current_score = 0
            return True
        elif choice == 'q':
            print(f"Thanks for playing! Total Score: {total_score}")
            return False
        else:
            print("Invalid choice. Please enter 'r', 'b', or 'q'.")
            return True


if __name__ == "__main__":
    invite_to_play()
    # play()
