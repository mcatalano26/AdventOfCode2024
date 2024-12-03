# https://adventofcode.com/2024/day/1

list1 = []
list2 = []

with open("input.txt", "r") as file:
	for i in file.readlines():
		list1.append(int(i.split()[0]))
		list2.append(int(i.split()[1]))
		
list1.sort()
list2.sort()

distance = 0

for count, val in enumerate(list1):
	distance += abs(val - list2[count])
	
print(distance)