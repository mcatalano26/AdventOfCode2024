# https://adventofcode.com/2024/day/2

from typing import List, Tuple

def problem_dampener_run_setup(lst: List, ind: int) -> Tuple[List, List]:
	lst1 = lst.copy()
	lst2 = lst.copy()
	lst1.pop(ind)
	lst2.pop(ind-1)
	return lst1, lst2

def is_safe(problem_dampener: bool, lst: List) -> bool:
	# check1 will check if our delta is at least 1 and at most 3
	# check2 will check that we're always increasing or decreasing
	check1 = 0
	check2 = 0

	for ind, curr in enumerate(lst):
		# If we're at the value 0, we don't have any good information yet
		if ind == 0:
			prev = curr
			continue
		if abs(prev - curr) <= 3 and abs(prev - curr) >= 1:
			check1 += 1
		elif problem_dampener:
			lst1, lst2 = problem_dampener_run_setup(lst, ind)
			if is_safe(False, lst1): return True
			elif is_safe(False, lst2): return True
			else: return False
		if prev-curr != 0:
			if prev-curr < 0:
				check2 += 1
			if prev-curr > 0:
				check2 -= 1
			if abs(check2) < ind:
				if problem_dampener:
					lst1, lst2 = problem_dampener_run_setup(lst, ind)
					if is_safe(False, lst1): return True
					elif is_safe(False, lst2): return True
					else: return False
		elif problem_dampener:
			lst1, lst2 = problem_dampener_run_setup(lst, ind)
			if is_safe(False, lst1): return True
			elif is_safe(False, lst2): return True
			else: return False
		prev = curr

	if abs(check1) == len(lst)-1 and abs(check2) == len(lst)-1:
		return True
	return False


with open("input.txt", "r") as file:
	safe_count = 0
	for i in file.readlines():

		problem_dampener = True
		lst = [int(x) for x in i.split()]

		if is_safe(problem_dampener, lst):
			safe_count += 1
		else:
			lst.pop(0)
			if is_safe(False, lst):
				safe_count += 1
	
	print(safe_count)
			