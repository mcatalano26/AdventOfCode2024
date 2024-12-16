# https://adventofcode.com/2024/day/2

from typing import List

def is_safe(row_number: int, problem_dampener: bool, lst: List) -> bool:
	first = True
	check1 = 0
	check2 = 0

	for ind, curr in enumerate(lst):
		if first:
			prev = curr
			first = False
			continue
		if abs(prev - curr) <= 3 and abs(prev - curr) >= 1:
			check1 += 1
		elif problem_dampener:
			print(f"lst {lst} is not safe. Popping {lst[ind]}")
			problem_dampener = False
			lst1 = lst.copy()
			lst2 = lst.copy()
			lst1.pop(ind)
			lst2.pop(ind-1)
			if is_safe(row_number, problem_dampener, lst1):
				return True
			elif is_safe(row_number, problem_dampener, lst2):
				return True
			else:
				return False
		if prev-curr != 0:
			if prev-curr < 0:
				check2 += 1
			if prev-curr > 0:
				check2 -= 1
			if abs(check2) < ind:
				if problem_dampener:
					print(f"lst {lst} is not safe. Popping {lst[ind]}")
					problem_dampener = False
					lst1 = lst.copy()
					lst2 = lst.copy()
					lst1.pop(ind)
					lst2.pop(ind-1)
					if is_safe(row_number, problem_dampener, lst1):
						return True
					elif is_safe(row_number, problem_dampener, lst2):
						return True
					else:
						return False
		elif problem_dampener:
			print(f"lst {lst} is not safe. Popping {lst[ind]}")
			problem_dampener = False
			lst1 = lst.copy()
			lst2 = lst.copy()
			lst1.pop(ind)
			lst2.pop(ind-1)
			if is_safe(row_number, problem_dampener, lst1):
				return True
			elif is_safe(row_number, problem_dampener, lst2):
				return True
			else:
				return False
		prev = curr

	if abs(check1) == len(lst)-1 and abs(check2) == len(lst)-1:
		print(f"lst {lst} is safe. Problem dampener = {problem_dampener}. Row number = {row_number}")
		return True
	print(f"lst {lst} is not safe. Problem dampener = {problem_dampener}. Row number = {row_number}")
	return False


with open("input.txt", "r") as file:
	safe_count = 0
	row_number = 1
	for i in file.readlines():
		# if row_number > 20:
		# 	break

		problem_dampener = True
		lst = [int(x) for x in i.split()]

		if is_safe(row_number, problem_dampener, lst):
			safe_count += 1
		else:
			lst.pop(0)
			problem_dampener = False
			print(f"first run wasn't safe...trying to pop 0th index and try again with problem_dampener off")
			if is_safe(row_number, problem_dampener, lst):
				safe_count += 1

		row_number += 1
	
	print(safe_count)
			