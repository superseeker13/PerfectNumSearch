import csv

def generateEvenPNums(num):
    generateEvenPNumsInRange(range(1, num+1))

#Range(start, end, 2)
def generateEvenPNumsInRange(rage):
    perfectList = list()
    for i in rage:
        print('i = ' + str(i))
        p = (2**i) - 1
        if isPrime(p):
            q = 2**(i-1)
            print('p, q = ', p, q)
            print(str(p*q) + ' is a perfect number.')
            perfectList.append(int(p*q))
            
    listToCsv(perfectList);

def searchOddPNumsInRange(rage):
    return   

def isPrime(num) -> bool:
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num <= 1:
        return False
    else:
        for i in [i for i in range(7, (int(num / 2) + 1), 2) if i % 3 != 0 or i % 5 != 0]:
            if num % i == 0:
                return False
    return True


def listToCsv(myList, fileName='perfectNums.csv'):
    with open(fileName, 'w', newline='') as myfile:
         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
         wr.writerow(myList)
