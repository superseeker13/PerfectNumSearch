# Consider renaming file
from csv import QUOTE_ALL, writer


def generateEvenPNums(num) -> list:
    return generateEvenPNumsInRange(range(1, num+1))


def generateEvenPNumsInRange(rage) -> list:
    perfectList = list()
    # Increases performace for large values
    append = perfectList.append
    for i in rage:
        if isMPrime(i):
            p = (2**i) - 1
            q = 2**(i-1)
            print('i, p, q = ', i, p, q)
            print(str(p*q) + ' is a perfect number.')
            append(int(p*q))
    listToCsv(perfectList)
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

# For general non-special primes
def isPrime(num) -> bool:
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num <= 1:
        return False
    else:
        gen = (i for i in range(7, (int(num / 2) + 1), 2) if i % 3 != 0)
        for i in gen:
            if num % i == 0:
                return False
    return True


def listToCsv(myList, fileName='perfectNums.csv'):
    with open(fileName, 'w', newline='') as myfile:
        wr = writer(myfile, quoting=QUOTE_ALL)
        wr.writerow(myList)
