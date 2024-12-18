# https://adventofcode.com/2024/day/2

from typing import List, Tuple
from icecream import ic

def problem_dampener_run(lst: List, ind: int) -> Tuple[List, List]:
	lst1 = lst.copy()
	lst2 = lst.copy()
	lst1.pop(ind)
	lst2.pop(ind-1)
	if is_safe(False, lst1): return True
	elif is_safe(False, lst2): return True
	else: return False

def is_safe(problem_dampener: bool, lst: List) -> bool:
	# check1 will check if our delta is at least 1 and at most 3
	# check2 will check that we're always increasing or decreasing
	check1, check2 = 0, 0

	for ind, curr in enumerate(lst):
		# If we're at the value 0, we don't have any good information yet
		if ind == 0:
			prev = curr
			continue
		if abs(prev - curr) <= 3 and abs(prev - curr) >= 1:
			check1 += 1
		elif problem_dampener: return problem_dampener_run(lst, ind)
		if prev-curr != 0:
			if prev-curr < 0: check2 += 1
			if prev-curr > 0: check2 -= 1
			if abs(check2) < ind:
				if problem_dampener: return problem_dampener_run(lst, ind)
		elif problem_dampener: return problem_dampener_run(lst, ind)
		prev = curr

	if abs(check1) == len(lst)-1 and abs(check2) == len(lst)-1: return True
	return False


def __main__():

	with open("input.txt", "r") as file:
		safe_count = 0
		for i in file.readlines():

			lst = [int(x) for x in i.split()]

			if is_safe(True, lst): safe_count += 1; continue

			lst.pop(0)

			if is_safe(False, lst): safe_count += 1
	return safe_count
	
ic(__main__())
			