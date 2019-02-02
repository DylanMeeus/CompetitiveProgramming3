# event planning
import sys

if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line)
    lines = list(filter(lambda k: k != "\n", lines))
    ptr = 0
    while ptr < len(lines):
        line = lines[ptr]
        if len(line.split(" ")) == 4:
            #print(line)
            data_line = line
            dparts = data_line.split(" ")
            participants = int(dparts[0])
            budget = int(dparts[1])
            hotels = int(dparts[2])
            total_cost = None 
            for hotel in range(hotels):
                ptr += 1
                price = int(lines[ptr].replace("\n",""))
                ptr += 1
                weekends = lines[ptr].replace("\n","")
                available_beds = list(map(lambda k: int(k), weekends.split(" ")))
                # if we have enough available beds, check the cost! 
                enough_beds = len(list(filter(lambda k: k >= participants, available_beds))) > 0
                if enough_beds:
                    hotel_cost = price * participants
                    if hotel_cost <= budget and (total_cost == None or hotel_cost < total_cost):
                        total_cost = hotel_cost
            print(total_cost if total_cost != None else "stay home")
            ptr += 1


