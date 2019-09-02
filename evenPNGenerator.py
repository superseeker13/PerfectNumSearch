import csv


def generateEvenPNums(num) -> list:
    return generateEvenPNumsInRange(range(1, num+1))


def generateEvenPNumsInRange(rage) -> list:
    perfectList = list()
    for i in rage:
        print('i = ' + str(i))
        p = (2**i) - 1
        if isPrime(p):
            q = 2**(i-1)
            print('p, q = ', p, q)
            print(str(p*q) + ' is a perfect number.')
            perfectList.append(int(p*q))
    listToCsv(perfectList)
    return perfectList


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
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(myList)
