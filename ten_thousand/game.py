from ten_thousand.game_logic import Game

def main():
    print("Welcome to Ten Thousand!")

    game = Game()

    while True:
        game.start_round()

        num_dice = int(input("Enter the number of dice to roll: "))
        dice_values = game.roll_dice(num_dice)

        choice = input("Do you want to set aside dice? (y/n): ").lower()
        if choice == 'y':
            dice_to_set_aside = tuple(map(int, input("Enter the dice values to set aside (space-separated): ").split()))
            game.set_aside(dice_to_set_aside)

        game.calculate_score_and_bank()

        if not game.next_round_or_quit():
            break

if __name__ == "__main__":
    main()
