#!/usr/bin/python3

# Question asked during baylabs interview.
# given a list of +- numbers, find the set of numbers which their sum
# is the greatest. 
""" Solution: doesn't really make sense, just add up all the positive numbers
              compute the power set, all permutations and get the sum
"""

def powerSet(items):
    list_len = len(items)
    for i in range(2**list_len):
        combo = []
        for j in range(list_len):
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2 # // floor division
        if a_list[midpoint] == item:
            found = True
            break
        else:
            if item < a_list[midpoint]:
                last = midpoint -1

            else:
                first = midpoint + 1
    return found


def main():
    items = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    x = powerSet(items)
    # for subset in x:
    #     total = sum(subset)
    #     if total == 12:
    #         print('subset: {subset}\t\t\t{total}'.format(total=total, subset=subset))
    is_found = binary_search(items, 5)
    print(is_found)

if __name__ == '__main__':
    main()
