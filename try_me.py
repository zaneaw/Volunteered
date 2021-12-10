import solution as sol


if __name__ == '__main__':

    start = int(input("What position do you want to start from? (Any number from 1-64)"))
    destination = int(input("What position do you want to the destination to be at? (ny number from 1-64)"))

    print(f"\nThe result of your input points, {start} and {destination}, are:\n-----------------------------------------------")

    start -= 1
    destination -= 1

    try_me = sol.solution(start, destination)
    print(f"\n-------------->    {try_me} moves\n")

