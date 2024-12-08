import re

with open('input.txt', 'r') as file:
    data = file.read()

do_matches = re.findall("do[(][)](.+?)don't[(][)]", data)

all_mul_matches = []

for do_match in do_matches:
    mul_matches = re.findall("mul[(][1-9]{1}[0-9]*,[1-9]{1}[0-9]*[)]", do_match)
    all_mul_matches.extend(mul_matches)

def mul(x, y):
    return x*y

total = 0

for mul_match in all_mul_matches:
    x, y = int(mul_match.split(",")[0][4:]), int(mul_match.split(",")[1][:-1])
    total += mul(x,y)

print(total)