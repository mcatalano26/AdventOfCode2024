import re

with open('input.txt', 'r') as file:
    data = file.read()

mul_matches = re.findall("mul[(][1-9]{1}[0-9]*,[1-9]{1}[0-9]*[)]", data)

def mul(x, y):
    return x*y

total = 0

for mul_match in mul_matches:
    x, y = int(mul_match.split(",")[0][4:]), int(mul_match.split(",")[1][:-1])
    total += mul(x,y)

print(total)