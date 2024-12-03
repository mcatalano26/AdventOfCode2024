# https://adventofcode.com/2024/day/1

dct = {}
lst = []

with open("input.txt", "r") as file:
	for i in file.readlines():
		dct[int(i.split()[0])] = 0
		lst.append(int(i.split()[1]))
		
for i in lst:
	if i in dct:
		dct[i] += 1

sim_score = 0	
for i, val in dct.items():
	sim_score += i*val

print(sim_score)
