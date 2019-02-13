# what's the median..

import sys
from statistics import median 
if __name__ == '__main__':
    nums = []
    for line in sys.stdin:
        # print median 
        nums.append(int(line.replace("\n","")))
        print(int(median(nums)))
