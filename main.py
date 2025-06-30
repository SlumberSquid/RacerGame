from typing import List
import racey_art
import time


def ascii_racer(track: List[str]) -> None:
    """
    Runs the tunnel game for a single session.
    """

    car_symbol = "A"
    car_col = 7  # Start in the center between tunnel walls at col 7
    row_index = 0
    laps = 0
    total_laps = 2
    track_len = len(track)

    print(racey_art.clear_screen_str)
    print(racey_art.car)
    print("Welcome to Tunnel Vision.")
    print("Navigate through to the light at the end of the tunnel to win!")
    print("Press 'a' for left, 'd' for right, enter for nothing.")
    print("If you hit the walls, you lose.")
    print("To win, you have to complete 2 laps around the tunnel array.")
    input("Press enter to start!")

    while True:
        print(racey_art.clear_screen_str)

        # Strip line number (first 2 chars) and grab tunnel
        line = track[row_index][2:]
        if car_col < 0 or car_col >= len(line) or line[car_col] != ' ':
            print(racey_art.skull)
            print("You crashed into the wall! Game Over.")
            return

        # Place the car on the line
        display_line = line[:car_col] + car_symbol + line[car_col + 1:]
        print(display_line)

        # Read movement input
        move = input()
        if move == 'a':
            car_col -= 1
        elif move == 'd':
            car_col += 1
        # else: no movement, but advance

        row_index += 1
        if row_index == track_len:
            row_index = 0
            laps += 1
            if laps == total_laps:
                print(racey_art.clear_screen_str)
                print(racey_art.win)
                print("You reached the light at the end of the tunnel! You win!")
                return


def prompt_replay() -> bool:
    """
    Prompts the user to play again. Only accepts 'y' or 'n'.
    Returns True to play again, False to exit.
    """
    while True:
        choice = input("Play again? (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            print("Thanks for playing Tunnel Vision!")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def main():
    while True:
        ascii_racer(racey_art.track)
        if not prompt_replay():
            break


if __name__ == "__main__":
    main()
