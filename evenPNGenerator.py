import matplotlib
from csv import QUOTE_NONE, writer
# import concurrent # Need to use multiprocesses # Ask Bilitski
import datetime

gui_env = ['TKAgg','GTKAgg','Qt4Agg','WXAgg']
matplotlib.use(gui_env[0],warn=False, force=True)

def generateEvenPNums(num) -> list:
    return generateEvenPNumsInRange(range(1, num+1))


def generateEvenPNumsInRange(rage) -> list:
    startTime = datetime.datetime.now()
    perfectList = list()
    # Increases performace for large values
    append = perfectList.append
    for i in rage:
        date = datetime.datetime.now()
        if isPrimeTrival(i) and isMPrime(i):
            p = (2**i) - 1
            q = 2**(i-1)
            print('Prime check time: ', datetime.datetime.now() - date)
            print('i, p, q = ', i, p, q)
            print(str(p*q) + ' is a perfect number.\n')
            append((i, int(p*q)))
    listToCsv(perfectList)
    print('Time to complete search:', datetime.datetime.now() - startTime)
    return perfectList

# For Mersenne primes uses the Lucas-Lehmer Test:
# Let n be an odd prime.
# The Mersenne number M(n) = 2**n-1 is prime if and only if
# S(n-2) = 0 (mod M(n)) where S(0) = 4 and S(k+1) = S(k)2-2.
def isMPrime(p) -> bool:
    s = 4
    m = 2**p -1
    for i in range(0, p-2):
        s = (s**2 - 2) % m
    return s == 0

def fermatPrimeCheck(num):
    return num % 4 == 1 and isPrimeTrival(num) or num == 2

def oddPerfectCheck(num) -> bool:
    if num % 2 == 1 and num > 10**1500:
        if modOddCheck(num):
            return fermatPrimeCheck(num)
    return False

def modOddCheck(num) -> bool:
    return num % 105 != 0 and num % 12 == 1 or \
           num % 468 == 117 or num % 324 == 81 \
           or num % 36 == 9

# For general non-special primes
def isPrimeTrival(num) -> bool:
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num <= 1:
        return False
    else:
        # executor = concurrent.futures.ProcessPoolExecutor(2)
        gen = (i for i in range(7, (int(num / 2) + 1), 2) if i % 3 != 0)
        for i in gen:
            if num % i == 0:
                return False
    return True

def scatterPlotList(_list):
    coords = list(zip(*_list))        
    matplotlib.pyplot.scatter(coords[0], coords[1])
    matplotlib.pyplot.show()

def listToCsv(myList, fileName='perfectNums.csv'):
    with open(fileName, 'w', newline='') as myfile:
        wr = writer(myfile, quoting=QUOTE_NONE, escapechar=' ')
        wr.writerow(myList)
