# https://adventofcode.com/2024/day/2

from typing import List
from icecream import ic

def is_safe(lst: List) -> bool:
	check1, check2 = 0, 0

	for ind, curr in enumerate(lst):
		if ind == 0: prev = curr; continue
		if abs(prev - curr) <= 3 and abs(prev - curr) >= 1: check1 += 1
		if prev-curr < 0: check2 += 1
		if prev-curr > 0: check2 -= 1
		prev = curr

	if abs(check1) == len(lst)-1 and abs(check2) == len(lst)-1: return True
	return False	

def __main__():
	with open("input.txt", "r") as file:
		safe_count = 0
		for i in file.readlines():

			lst = [int(x) for x in i.split()]
			
			if is_safe(lst): safe_count += 1
		
	return safe_count

ic(__main__())
			