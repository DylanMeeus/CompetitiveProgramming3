import sys

def solve(data):
    # find out when the snail leaves, or fails
    snail_height = 0
    height_well = data[0]
    day_distance = data[1]
    slide_distance = data[2]
    fatigue = data[3]
    day_decrease = day_distance * fatigue/100
    day = 1
    while True:
        if day_distance > 0:
            snail_height += day_distance
        if snail_height > height_well:
            return "success on day {}".format(day)
        day_distance -= day_decrease 
        snail_height -= slide_distance
        if snail_height < 0:
            return "failure on day {}".format(day)
        day += 1




if __name__ == '__main__':
    data = [list(map(lambda k: int(k), filter(lambda k: k != "", line.replace("\n","").split(" ")))) for line in sys.stdin]
    for d in data:
        if d[0] == 0:
            exit()
        solution = solve(d)
        print(solution)


