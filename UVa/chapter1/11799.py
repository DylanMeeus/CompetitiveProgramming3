import sys

if __name__ == '__main__':
    case = 0
    for line in sys.stdin:
        if case == 0:
            # skip the first one
            case += 1
            continue
        m = max(list(map(lambda k: int(k), line.split(" "))))
        print("Case {}: {}".format(case,m))
        case += 1


