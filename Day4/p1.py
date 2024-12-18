# https://adventofcode.com/2024/day/2

from typing import List
from icecream import ic

def get_columns(matrix: List[List[str]]) -> List[List[str]]:
    columns = []
    for i in range(len(matrix)):
        columns.append([row[i] for row in matrix])
    return columns

def straight_matches(row: List[str]) -> int:
    matches = 0
    for ind, letter in enumerate(row):
        if letter == "X":
            try:
                if row[ind+1] == "M":
                    if row[ind+2] == "A":
                        if row[ind+3] == "S":
                            matches += 1
            except IndexError:
                continue
    return matches

def down_right_diagonal_matches(matrix: List[List[str]]) -> int:
    matches = 0
    for row_id, row in enumerate(matrix):
            for column_id, letter in enumerate(row):
                  if letter == "X":
                        try:
                              if matrix[row_id+1][column_id+1] == "M" and matrix[row_id+2][column_id+2] == "A" and matrix[row_id+3][column_id+3] == "S":
                                    matches += 1
                        except IndexError:
                              continue
    return matches

def up_right_diagonal_matches(matrix: List[List[str]]) -> int:
    matches = 0
    for row_id, row in enumerate(matrix):
            for column_id, letter in enumerate(row):
                  if letter == "X":
                        if row_id-3>=0:
                            try:
                                if matrix[row_id-1][column_id+1] == "M" and matrix[row_id-2][column_id+2] == "A" and matrix[row_id-3][column_id+3] == "S":
                                        matches += 1
                            except IndexError:
                                continue
    return matches

def up_left_diagonal_matches(matrix: List[List[str]]) -> int:
    matches = 0
    for row_id, row in enumerate(matrix):
            for column_id, letter in enumerate(row):
                  if letter == "X":
                        if column_id-3>=0 and row_id-3>=0:
                            try:
                                if matrix[row_id-1][column_id-1] == "M" and matrix[row_id-2][column_id-2] == "A" and matrix[row_id-3][column_id-3] == "S":
                                        matches += 1
                            except IndexError:
                                continue
    return matches

def down_left_diagonal_matches(matrix: List[List[str]]) -> int:
    matches = 0
    for row_id, row in enumerate(matrix):
            for column_id, letter in enumerate(row):
                  if letter == "X":
                        if column_id-3>=0:
                            try:
                                if matrix[row_id+1][column_id-1] == "M" and matrix[row_id+2][column_id-2] == "A" and matrix[row_id+3][column_id-3] == "S":
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
    prev = 0
    for row in matrix:
        matches += straight_matches(row)

    for row in matrix:
        reverse_row = row[::-1]
        matches += straight_matches(reverse_row)

    columns = get_columns(matrix)

    for column in columns:
          matches += straight_matches(column)

    for column in columns:
          reverse_column = column[::-1]
          matches += straight_matches(reverse_column)

    matches += down_right_diagonal_matches(matrix)
    matches += up_right_diagonal_matches(matrix)
    matches += down_left_diagonal_matches(matrix)
    matches += up_left_diagonal_matches(matrix)

    return matches
	
ic(__main__())