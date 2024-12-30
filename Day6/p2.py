from icecream import ic
import itertools

from p1 import Direction
from p1 import spaces_touched, paint_matrix


def __main__():
    obstacles = []
    with open("test_input.txt", "r") as file:
        matrix = []
        for x, line in enumerate(file.readlines()):
            row = list(line.rstrip())
            matrix.append(row)
            for y, pos in enumerate(row):
                if pos == "#":
                    obstacles.append((x, y))
                if pos == "^":
                    current_pos = (x, y)

    starting_current_pos = current_pos

    distinct_spaces = set()
    order_of_turns = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
    
    matrix_with_obstacle = matrix.copy()

    infinite_loop_count = 0

    for x, row in enumerate(matrix):
        for y, _ in enumerate(row):
            if matrix[x][y] == ".":
                matrix_with_obstacle[x][y] = "#"
    
                consecutive_no_spaces_added = 0
                for direction in itertools.cycle(order_of_turns):
                    spaces_added = False
                    spaces_to_add, current_pos, hit_obstacle = spaces_touched(current_pos, obstacles, matrix_with_obstacle, direction)
                    for space in spaces_to_add:
                        spaces_added = True
                        consecutive_no_spaces_added = 0
                        distinct_spaces.add(space)
                    
                    if not spaces_added:
                        consecutive_no_spaces_added += 1
                    
                    if consecutive_no_spaces_added == 4:
                        infinite_loop_count += 1
                        break

                    if not hit_obstacle:
                        break

    painted_matrix = paint_matrix(matrix, distinct_spaces, starting_current_pos)

    print(f'ANSWER: {infinite_loop_count}')

    # return a painted matrix when you want to see the full path visually
    return painted_matrix
    # return True
		
ic(__main__())