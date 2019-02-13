# detect jolly jumpers
import sys
from functools import reduce


def is_jolly(nums):
    if len(nums) == 1:
        return True
    # else check the diffs
    mask = [False for x in range(len(nums))]
    mask[0] = True # the zero diff does not count
    i = 0
    j = 1
    while j < len(nums):
        diff = abs(nums[j] - nums[i])
        if diff < len(mask):
            mask[diff] = True
        i += 1
        j += 1
    # The first element does not matter
    return reduce(lambda a, b: a and b, mask)




if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line)

    for line in lines:
        parts = line.replace("\n","").split(" ")
        parts = list(map(lambda k: int(k), parts))
        jolly = is_jolly(parts[1:])
        if jolly:
            print("Jolly")
        else:
            print("Not jolly")





