# https://adventofcode.com/2024/day/2

from typing import List

def is_safe(problem_damper: bool, lst: List) -> bool:
	print(lst)
	first = True
	check1 = 0
	check2 = 0

	for i, j in enumerate(lst):
		if first:
			current = j
			first = False
			continue
		if abs(current - j) <= 3 and abs(current - j) >= 1:
			check1 += 1
		elif problem_damper:
			new_lst = lst[:i] + lst[i+1:]
			return is_safe(False, new_lst)
		if current-j < 0 or current-j > 0:
			if current-j < 0:
				check2 += 1
			if current-j > 0:
				check2 -= 1
		if abs(check2) < i and problem_damper:
			new_lst = lst[:i] + lst[i+1:]
			print('new_lst 2')
			print(new_lst)
			return is_safe(False, new_lst)
		current = j

	if abs(check1) == len(lst)-1 and abs(check2) == len(lst)-1:
		return True
	return False	




with open("test_input.txt", "r") as file:
	safe_count = 0
	for i in file.readlines():

		problem_damper = True
		lst = [int(x) for x in i.split()]
		
		if is_safe(problem_damper, lst):
			safe_count += 1
	
	print(safe_count)