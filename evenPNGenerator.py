from csv import QUOTE_NONE, writer
import concurrent
import datetime


def generateEvenPNums(num) -> list:
    return generateEvenPNumsInRange(range(5, num+1))


def generateEvenPNumsInRange(rage) -> list:
    perfectList = list()
    # Increases performace for large values
    append = perfectList.append
    for i in rage:
        p = (2**i) - 1
        date = datetime.datetime.now()
        if isPrime(p):
            q = 2**(i-1)
            print('Prime check time: ', datetime.datetime.now() - date)
            print('i, p, q = ', i, p, q)
            print(str(p*q) + ' is a perfect number.\n')
            append(int(p*q))
    listToCsv(perfectList)
    return perfectList


def isPrime(num) -> bool:
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


def listToCsv(myList, fileName='perfectNums.csv'):
    with open(fileName, 'w', newline='') as myfile:
        wr = writer(myfile, quoting=QUOTE_NONE)
        wr.writerow(myList)
