# solutions to Excercise 1.2.3

# Try to write these solutions as concise as possible.

# 2. given a date, determine the day of the week.
import datetime
def dayOfWeek():
    d = datetime.datetime.strptime("23/01/2019", "%d/%m/%Y")
    return d.strftime("%A")


