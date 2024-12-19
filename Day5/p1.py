# https://adventofcode.com/2024/day/2

from icecream import ic

def is_correctly_ordered(page_lst: list, rules_dct: dict[list[str]]) -> int:
    for i, page in enumerate(page_lst):
        if i == len(page_lst)-1:
            break
        if page in rules_dct:
            must_come_before = rules_dct[page]
            for x in must_come_before:
                if x in page_lst[i+1:]:
                    return 0
    return int(page_lst[int(len(page_lst)/2)])

def __main__():
    with open("rules.txt", "r") as file:
        rules_dct = {}
        for line in file.readlines():
            before, after = line.rstrip().split("|")[0], line.rstrip().split("|")[1]
            if after not in rules_dct:
                rules_dct[after] = [before]
            else:
                rules_dct[after].append(before)

    with open("pages.txt", "r") as file:
        total_count = 0
        for line in file.readlines():
            page_lst = line.rstrip().split(",")
            total_count += is_correctly_ordered(page_lst, rules_dct)
            

    return total_count
		
ic(__main__())