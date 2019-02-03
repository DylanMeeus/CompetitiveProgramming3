import sys


def depr(month, rec_data):
    cp = 0.0 
    cp = float(rec_data[0].split(" ")[1])
    for line in rec_data:
        m = line.split(" ")[0]
        p = line.split(" ")[1]
        if int(m) < month:
            cp = float(p)
        else:
            break
    return cp


def sim(duration, down_pay, am, rec_data):
    months = 0
    # down_pay is what is removed from am each month
    # and the value goes down by depr rate?
    value = am + down_pay 
    value = value - (value * depr(months, rec_data))
    rem_cost = am - down_pay 
    loan_cost = (am - down_pay) / duration
    months = 1
    while rem_cost >= value:
        months += 1
        rem_cost -= loan_cost
        value = value - (value * depr(months, rec_data))  
    return months


if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line)

    duration = 0
    down_payment = 0
    amount = 0
    following_records = 0 # don't need it brah
    ptr = 0
    while ptr < len(lines):
        line = lines[ptr]
        parts = line.split(" ")
        if len(parts) == 4:
            duration = int(parts[0])
            if duration < 0:
                exit()
            down_payment = float(parts[1])
            amount = float(parts[2])
            following_records = int(parts[3])
            ptr += 1
            continue
        else:
            rules = []
            while following_records > 0:
                line = lines[ptr]
                rules.append(line)
                following_records -= 1
                ptr += 1
            # now simulate
            rules = list(map(lambda k: k.replace("\n",""), rules))
            res = (sim(duration,down_payment,amount,rules))
            print(str(res) + (" month" if res < 2 else " months"))
