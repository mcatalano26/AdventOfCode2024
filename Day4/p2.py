# https://adventofcode.com/2024/day/2

from typing import List
from icecream import ic

def down_right_diagonal_matches(matrix: List[List[str]]) -> int:
    matches = 0
    for row_id, row in enumerate(matrix):
            for column_id, letter in enumerate(row):
                  if letter == "M":
                        try:
                              if matrix[row_id+1][column_id+1] == "A" and matrix[row_id+2][column_id+2] == "S":
                                    if matrix[row_id+2][column_id] == "M" and matrix[row_id+1][column_id+1] == "A" and matrix[row_id][column_id+2] == "S":
                                        matches += 1
                                    if matrix[row_id][column_id+2] == "M" and matrix[row_id+1][column_id+1] == "A" and matrix[row_id+2][column_id] == "S":
                                        matches += 1
                        except IndexError:
                              continue
    return matches

def up_left_diagonal_matches(matrix: List[List[str]]) -> int:
    matches = 0
    for row_id, row in enumerate(matrix):
            for column_id, letter in enumerate(row):
                  if letter == "M":
                        if column_id-2>=0 and row_id-2>=0:
                            try:
                                if matrix[row_id-1][column_id-1] == "A" and matrix[row_id-2][column_id-2] == "S":
                                    if matrix[row_id][column_id-2] == "M" and matrix[row_id-1][column_id-1] == "A" and matrix[row_id-2][column_id] == "S":
                                        matches += 1
                                    if matrix[row_id-2][column_id] == "M" and matrix[row_id-1][column_id-1] == "A" and matrix[row_id][column_id-2] == "S":
                                        matches += 1
                            except IndexError:
                                continue
    return matches

def __main__():
    with open("input.txt", "r") as file:
        matrix = []
        for line in file.readlines():
            row = list(line.rstrip())
            matrix.append(row)
		
    matches = 0

    matches += down_right_diagonal_matches(matrix)
    matches += up_left_diagonal_matches(matrix)

    return matches
	
ic(__main__())