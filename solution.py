##############################################################################
####################### Google Foobar Coding Challenge #######################
##############################################################################
# Implementation of Breadth First Search algorithm
from collections import deque

# Increase the size of the board here
board = 8

# Don't change below this line!!!!
board_max = board * board - 1

row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]


# Initiate the Node object to keep track of where the Knight has moved.
# This GREATLY cuts down on runtime. The reason is because it stores the moves that have already been made. This way, we can't retrace our steps and every move that is made is a new move, progress towards an answer will be made with every step.
class Node:
    def __init__(self, x, y, dist=0):
        self.x = x       # x coordinate
        self.y = y       # y coordinate
        self.dist = dist # tracks amount of moves made to get to current point

# Check if the coordinates the Knight is going to are valid
def is_valid(x, y, board):
    return not (x < 0 or y < 0 or x >= board or y >= board)


def solution(start, end):
    if start > board_max or end > board_max or start < 0 or end < 0:
        return "Start point or destination point unreachable. Please try again"
    # Convert the start and end to (x, y) coordinates
    start_x, end_x = start // board, end // board
    start_y, end_y = start % board, end % board
    # Create the objects
    start, end = Node(start_x, start_y), Node(end_x, end_y)
    visited = set()
    # Documentation reference link at bottom
    q = deque()
    # Add 'start' node to the queue
    q.append(start)

    while q:
        node = q.popleft() # Optimization over q.pop(0)
        x = node.x
        y = node.y
        dist = node.dist
        # Jackpot!
        if x == end.x and y == end.y:
            return dist
        # 
        if node not in visited:
            visited.add(node) # More optimization
            for i in range(8): # iterate over row and col
                x1 = x + row[i]
                y1 = y + col[i]
                # call is_valid function to ensure coords are on board
                if is_valid(x1, y1, board):
                    q.append(Node(x1, y1, dist + 1))



if __name__ == '__main__':
    print(solution(0, 62))
    '''
    Call the function with 2 arguments.
    The arguments you give are coordinates to Point A and Point B.
    Such that a Chessboard is labeled like below:
    -------------------------
    | 0| 1| 2| 3| 4| 5| 6| 7|   <- solution(0, 1)
    -------------------------
    | 8| 9|10|11|12|13|14|15|
    -------------------------
    |16|17|18|19|20|21|22|23|
    -------------------------
    |24|25|26|27|28|29|30|31|
    -------------------------
    |32|33|34|35|36|37|38|39|
    -------------------------
    |40|41|42|43|44|45|46|47|
    -------------------------
    |48|49|50|51|52|53|54|55|
    -------------------------
    |56|57|58|59|60|61|62|63|
    -------------------------
    '''