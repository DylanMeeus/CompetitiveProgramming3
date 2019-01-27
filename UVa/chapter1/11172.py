import sys

if __name__ == '__main__':
    statements = []
    for line in sys.stdin:
        statements.append(line)

    ptr = 1
    while ptr < len(statements):
        s = statements[ptr]
        parts = s.split(" ")
        fst, snd = int(parts[0]), int(parts[1])
        if fst == snd:
            print("=")
        elif fst > snd:
            print(">")
        else:
            print("<")
        ptr += 1

