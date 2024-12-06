# https://adventofcode.com/2024/day/2

with open("input.txt", "r") as file:
	safe_count = 0
	for i in file.readlines():
		# abs value of check1 and check2 must be len(lst) - 1 for the report to be 'safe'
		check1 = 0
		check2 = 0
		first = True

		lst = [int(x) for x in i.split()]

		for j in lst:
			if first:
				current = j
				first = False
				continue
			if abs(current - j) <= 3 and abs(current - j) >= 1:
				check1 += 1
			if current-j < 0:
				check2 += 1
			if current-j > 0:
				check2 -= 1
			current = j

		if abs(check1) == len(lst)-1 and abs(check2) == len(lst)-1:
			safe_count += 1
	
	print(safe_count)
			