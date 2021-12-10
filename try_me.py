import solution as sol
from time import sleep


if __name__ == '__main__':
    print("\n\n*** READ BELOW BEFORE USING ***")
    sleep(1)
    print("\n\nYour computer will slow significantly down if you try a board size that is too large. For board size, try not to go above 14. IF you do try 14, don't try 1 and 196 as the two coordinates! This could take up to 60 seconds or longer to complete.\n")
    # sleep(12)
    board = int(input(f"\nWhat size board would you like to try? "))
    board_max = board**2
    start = int(input(f"\nWhat position do you want to start from? (Any number from 1-{board_max}) "))
    destination = int(input(f"\nWhat position do you want to the destination to be at? (Any number from 1-{board_max}) "))

    print(f"\nThe result of your input points, {start} and {destination}, are:\n------------------------------------------------")


    start -= 1
    destination -= 1

    try_me = sol.solution(start, destination, board)
    print(f"\n-------------------------->    {try_me} moves\n")

