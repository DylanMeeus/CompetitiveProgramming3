# solutions to Excercise 1.2.3

# Try to write these solutions as concise as possible.

# 3. given a date, determine the day of the week.
import datetime
import random
from itertools import permutations
def ex3():
    d = datetime.datetime.strptime("23/01/2019", "%d/%m/%Y")
    return d.strftime("%A")

# 4. Given n random integers, print the distinct (unique) integers in sorted order
def ex4():
    rs = [random.randint(0,9) for x in range(100)]
    print(set(rs)) # set will keep them sorted and unique ;-)

# 5. Given distinct birthdates as triples, sort them first by month, then day and then year. (asc)
def ex5():
    bdays = [(1, 7, 1992), (1, 11, 1988), (20,7,1934)]
    print(sorted(bdays, key=lambda b: (b[1], b[0], b[2])))

# 6. Given a list of (sorted) integers L of size 1M, determine if V exists in less than 20
# comparisons
def ex6():
    L = sorted([random.randint(0,10**6) for x in range(10**6)])
    S = L[random.randint(0,len(L))] # be sure that S is contained in L
    # in the real world: t print(True if S in L else False)
    # Binary search should be fine for this problem. (20 times taking half is < 1, thus it should
    # have matched the number for sure). 10^6 / (2^20)
    size = len(L)
    ptr = size
    for i in range(20):
        ptr = ptr // 2
        if L[ptr] == S:
            return True
        elif len(L) == 0:
            return False

        if S > L[ptr]:
            L = L[ptr:]
        elif S < L[ptr]:
            L = L[:ptr]
    return False


# 7. Generate all permutations of 'A', 'B', .. 'J'. 

def ex7():
    L = ['A','B','C','D','E','F','G','H','I','J']
    print(list(permutations(L)))

def ex11():
    eq = "3 + (8 - 7.5) * 10 / 5 - (2+5*7)"
    print(eval(eq))

ex11()
