# solutions to Excercise 1.2.3

# Try to write these solutions as concise as possible.

# 3. given a date, determine the day of the week.
import datetime
import random
def ex3():
    d = datetime.datetime.strptime("23/01/2019", "%d/%m/%Y")
    return d.strftime("%A")

# 4. Given n random integers, print the distinct (unique) integers in sorted order
def ex4():
    rs = [random.randint(0,9) for x in range(100)]
    print(set(rs)) # set will keep them sorted and unique ;-)

