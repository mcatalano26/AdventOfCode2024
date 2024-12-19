# https://adventofcode.com/2024/day/2

from icecream import ic

def is_correctly_ordered(page_lst: list, rules_dct: dict[list[str]]) -> bool:
    for i, page in enumerate(page_lst):
        if i == len(page_lst)-1:
            break
        if page in rules_dct:
            must_come_before = rules_dct[page]
            for x in must_come_before:
                if x in page_lst[i+1:]:
                    return False
    return True

def order_page_lst(page_lst: list, rules_dct: dict[list[str]]) -> list:
    for i, page in enumerate(page_lst):
        if i == len(page_lst)-1:
            break
        if page in rules_dct:
            must_come_before = rules_dct[page]
            for ii, x in enumerate(page_lst[i+1:]):
                if x in must_come_before:
                    new_lst = page_lst.copy()
                    new_lst[i] = x
                    new_lst[ii+i+1] = page
                    return order_page_lst(new_lst, rules_dct)
    return page_lst

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
        incorrectly_ordered_page_lsts = []
        for line in file.readlines():
            page_lst = line.rstrip().split(",")
            if not is_correctly_ordered(page_lst, rules_dct):
                incorrectly_ordered_page_lsts.append(page_lst)

    total_count = 0
    for page_lst in incorrectly_ordered_page_lsts:
        ordered_lst = order_page_lst(page_lst, rules_dct)
        total_count += int(ordered_lst[int(len(ordered_lst)/2)])

    return total_count
		
ic(__main__())