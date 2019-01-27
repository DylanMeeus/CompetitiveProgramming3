import sys

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        data.append(line)

    ptr = 1
    while ptr < len(data):
        costs = set(map(lambda k: int(k), data[ptr].split(" ")))
        costs -= {min(costs),max(costs)}
        print("Case {}:".format(ptr) + " " + str(list(costs)[0]))
        ptr += 1


