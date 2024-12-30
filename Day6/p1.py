# https://adventofcode.com/2024/day/6

from icecream import ic
from enum import Flag, auto
import itertools

class Direction(Flag):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()

# spaces_touched_* functions will return:
# # list of the spaces touched
# # the new current position
# # whether we have left the map

def spaces_touched_going_up(current_pos: tuple, obstacles: list[tuple], map: list[list], closest_obstacle: tuple, obstacle_hit=True, spaces_to_add=set()) -> set | tuple | bool:
    for obstacle in obstacles:
        if obstacle[1] == current_pos[1]:
            if obstacle[0] < current_pos[0]:
                if closest_obstacle == current_pos:
                    closest_obstacle = obstacle
                else:
                    if obstacle[0] > closest_obstacle[0]:
                        closest_obstacle = obstacle
    if closest_obstacle == current_pos:
        obstacle_hit = False
        new_current_pos = (-1, -1)
    else:
        new_current_pos = (closest_obstacle[0]+1, closest_obstacle[1])
    
    if obstacle_hit:
        for i in range(abs(closest_obstacle[0]-current_pos[0])):
            spaces_to_add.add((current_pos[0]-i, current_pos[1]))
    else:
        for i in range(current_pos[0]+1):
            spaces_to_add.add((current_pos[0]-i, current_pos[1]))

    return spaces_to_add, new_current_pos, obstacle_hit

def spaces_touched_going_down(current_pos: tuple, obstacles: list[tuple], map: list[list], closest_obstacle: tuple, obstacle_hit=True, spaces_to_add=set()) -> set | tuple | bool:
    for obstacle in obstacles:
        if obstacle[1] == current_pos[1]:
            if obstacle[0] > current_pos[0]:
                if closest_obstacle == current_pos:
                    closest_obstacle = obstacle
                else:
                    if obstacle[0] < closest_obstacle[0]:
                        closest_obstacle = obstacle
    if closest_obstacle == current_pos:
        obstacle_hit = False
        new_current_pos = (-1, -1)
    else:
        new_current_pos = (closest_obstacle[0]-1, closest_obstacle[1])
    
    if obstacle_hit:
        for i in range(abs(closest_obstacle[0]-current_pos[0])):
            spaces_to_add.add((current_pos[0]+i, current_pos[1]))
    else:
        for i in range(abs(current_pos[0]-len(map))):
            spaces_to_add.add((current_pos[0]+i, current_pos[1]))
    return spaces_to_add, new_current_pos, obstacle_hit

def spaces_touched_going_right(current_pos: tuple, obstacles: list[tuple], map: list[list], closest_obstacle: tuple, obstacle_hit=True, spaces_to_add=set()) -> set | tuple | bool:
    for obstacle in obstacles:
        if obstacle[0] == current_pos[0]:
            if obstacle[1] > current_pos[1]:
                if closest_obstacle == current_pos:
                    closest_obstacle = obstacle
                else:
                    if obstacle[1] < closest_obstacle[1]:
                        closest_obstacle = obstacle
    if closest_obstacle == current_pos:
        obstacle_hit = False
        new_current_pos = (-1, -1)
    else:
        new_current_pos = (closest_obstacle[0], closest_obstacle[1]-1)
    
    if obstacle_hit:
        for i in range(abs(closest_obstacle[1]-current_pos[1])):
            spaces_to_add.add((current_pos[0], current_pos[1]+i))
    else:
        for i in range(abs(current_pos[1]-len(map[0]))):
            spaces_to_add.add((current_pos[0], current_pos[1]+i))
    return spaces_to_add, new_current_pos, obstacle_hit

def spaces_touched_going_left(current_pos: tuple, obstacles: list[tuple], map: list[list], closest_obstacle: tuple, obstacle_hit=True, spaces_to_add=set()) -> set | tuple | bool:
    for obstacle in obstacles:
        if obstacle[0] == current_pos[0]:
            if obstacle[1] < current_pos[1]:
                if closest_obstacle == current_pos:
                    closest_obstacle = obstacle
                else:
                    if obstacle[1] > closest_obstacle[1]:
                        closest_obstacle = obstacle
    if closest_obstacle == current_pos:
        obstacle_hit = False
        new_current_pos = (-1, -1)
    else:
        new_current_pos = (closest_obstacle[0], closest_obstacle[1]+1)
    
    if obstacle_hit:
        for i in range(abs(closest_obstacle[1]-current_pos[1])):
            spaces_to_add.add((current_pos[0], current_pos[1]-i))
    else:
        for i in range(abs(current_pos[1]+1)):
            spaces_to_add.add((current_pos[0], current_pos[1]-i))
    return spaces_to_add, new_current_pos, obstacle_hit

def spaces_touched(current_pos: tuple, obstacles: list[tuple], map: list[list], direction: str) -> set | tuple | bool:
    closest_obstacle = current_pos

    if direction == Direction.UP:
        return spaces_touched_going_up(current_pos, obstacles, map, closest_obstacle)
    if direction == Direction.DOWN:
        return spaces_touched_going_down(current_pos, obstacles, map, closest_obstacle)
    if direction == Direction.RIGHT:
        return spaces_touched_going_right(current_pos, obstacles, map, closest_obstacle)
    if direction == Direction.LEFT:
        return spaces_touched_going_left(current_pos, obstacles, map, closest_obstacle)

# Used to see the full path visually
def paint_matrix(matrix: list[list], distinct_spaces: list[tuple], starting_current_pos: tuple) -> list[list]:
    for space in distinct_spaces:
        matrix[space[0]][space[1]] = 'X'

    matrix[starting_current_pos[0]][starting_current_pos[1]] = '^'

    return matrix

def __main__():
    obstacles = []
    with open("input.txt", "r") as file:
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
    
    for direction in itertools.cycle(order_of_turns):
        spaces_to_add, current_pos, hit_obstacle = spaces_touched(current_pos, obstacles, matrix, direction)
        for space in spaces_to_add:
            distinct_spaces.add(space)
        
        if not hit_obstacle:
            break

    painted_matrix = paint_matrix(matrix, distinct_spaces, starting_current_pos)

    print(f'ANSWER: {len(distinct_spaces)}')

    # return a painted matrix when you want to see the full path visually
    # return painted_matrix
    return True
		
ic(__main__())