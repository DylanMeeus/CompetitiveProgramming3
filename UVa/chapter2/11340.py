# newspaper
import sys



def score(key, sentence):
    scores = list(map(lambda k:key[k] if k in key else 0, sentence))
    return sum(scores)

if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line)
    
    tests = int(lines[0])
    ptr = 1
    currentSet = None
    currentSentence = None
    currentKey = {}
    currentScore = 0
    while ptr < len(lines):
        if currentSet == None:
            currentSet = int(lines[ptr])
            ptr += 1
            for i in range(currentSet):
                # each line should be parsed
                score_key_line = lines[ptr]
                parts = score_key_line.replace("\n","").split(" ")
                currentKey[parts[0]] = int(parts[1]) 
                ptr += 1
        elif currentSentence == None:
            currentSentence = int(lines[ptr])
            ptr += 1
            for i in range(currentSentence):
                # join all lines
                currentScore += score(currentKey, lines[ptr])
                ptr += 1
            currentSet = None
            currentSentence = None
            print("{0:.2f}$".format(float(currentScore) / 100))
            # now next round
            currentSet = None
            currentSentence = None
            currentKey = {}
            currentScore = 0



