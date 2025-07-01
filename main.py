#THIS IS THE IMPORT LIST

from typing import List
import racey_art
import sys
import select

#THIS PUSHES THE GAME FORWARD REGARDLESS OF INPUT

def get_input(timeout=0.5) -> str:
   
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n')
    else:
        return ''

def ascii_racer(track: List[str]) -> None:
    
#THIS IS THE INTRO SCREEN TO THE PROGRAM 

    print(racey_art.clear_screen_str)
    print(racey_art.car)
    print("Welcome to Tunnel Vision.")
    print("Navigate through to the light at the end of the tunnel to win!")
    print("Press 'a' for left, 'd' for right, enter for nothing.")
    print("If you hit the walls, you lose.")
    print("To win, you have to complete 2 laps around the tunnel array.")
    input("Press enter to start!")

#THIS IS THE ITEMS DEFINED BEFORE THE PROGRAM ACTUALLY RUNS

    car = "^"
    car_col = 7
    row = 0
    laps = 0
    total_laps = 2
    track_len = len(track)

#THIS IS THE RULES TO GET A GAME OVER

    while True:
        print(racey_art.clear_screen_str)

        current_line = track[row][2:]
        if car_col < 0 or car_col >= len(current_line) or current_line[car_col] != ' ':
            print(racey_art.skull)
            print("You crashed into the wall! Game Over.")
            return

#THIS SHOWS THE CARS ROW AND THE TWO ROWS AHEAD AND ALSO THE LIGHTBULB TO GIVE ILLUSIION OF TERMINAL NOT REFRESHING

        lines_to_display = []
        for offset in range(-2, 1):  # -2, -1, 0
            idx = (row + offset) % track_len
            line = track[idx][2:]
            if offset == 0:
                display_line = line[:car_col] + car + line[car_col + 1:]
            else:
                display_line = line
            lines_to_display.append(display_line)

        print(racey_art.lightbulb)
        for display_line in lines_to_display:
            print(display_line)

#THIS IS THE MOVEMENT INPUT IT WILL MOVE CAR WITH OR WITHOUT INPUT

        move = get_input(0.5)
        if move == 'a':
            car_col -= 1
        elif move == 'd':
            car_col += 1

        row += 1
        if row == track_len:
            row = 0
            laps += 1

            if laps == total_laps:
                print(racey_art.clear_screen_str)
                print(racey_art.win)
                print("You reached the light at the end of the tunnel! You win!")
                return

#THIS IS THE "DO YOU WANT TO PLAY AGAIN" AFTER CRASHING INTO WALL USING BOOL

def prompt_replay() -> bool:
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            print("Thank you for playing Tunnel Vision PROGRAM. End of line.")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

#THIS SECTION CLEARS AND RESETS THE PROGRAM (SIMPLE RESET)

def main():
    while True:
        ascii_racer(racey_art.track)
        if not prompt_replay():
            break

#THIS IS THE ACTUAL BEGINNING

if __name__ == "__main__":
    main()
