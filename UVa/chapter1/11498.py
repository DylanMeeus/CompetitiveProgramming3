import sys

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        data.append(line)
    ptr = 0
    currentDivisor = None
    while data[ptr] != "0\n":
        entry = data[ptr].split(" ")
        if len(entry) == 1:
            currentDivisor = None
            ptr += 1
            continue
        if currentDivisor == None: 
            cx, cy = int(entry[0]), int(entry[1])
            currentDivisor = (cx, cy)
        else:
            # check where our point is relative to the divisor
            px, py = int(entry[0]), int(entry[1])
            if px < currentDivisor[0] and py < currentDivisor[1]:
                print("SO")
            elif px < currentDivisor[0] and py > currentDivisor[1]:
                print("NO")
            elif px > currentDivisor[0] and py < currentDivisor[1]:
                print("SE")
            elif px > currentDivisor[0] and py > currentDivisor[1]:
                print("NE")
            elif px == currentDivisor[0] or py == currentDivisor[1]:
                print("divisa")
        ptr += 1


            



