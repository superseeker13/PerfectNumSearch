import matplotlib
from csv import QUOTE_NONE, writer


def main():
    
    # Check for the proper gui
    # From stack overflow Rolf of Saxony
    gui_env = ['TKAgg','GTKAgg','Qt4Agg','WXAgg']
    for gui in gui_env:
        try:
            print("testing", gui)
            matplotlib.use(gui,warn=False, force=True)
            from matplotlib import pyplot as plt
            break
        except:
            continue
    print("Using:",matplotlib.get_backend())
    
def generateDivisorSum(num):
    print('Sum of even numbered divisors in range')
    return generateDivisorSumRange(range(0,num,2))

def generateDivisorSumRange(rage):
    oddList = list()
    evenList = list()
    for i in rage:
        total = sum(z for z in range(1,i) if i % z == 0)
        if total % 2 == 0:
            evenList.append((i, total))
        elif total != 0:
            oddList.append((i, total))

    listToCsv(evenList, fileName='evenDivisorSum.csv')
    listToCsv(oddList, fileName='oddDivisorSum.csv')
    print('Odd, Even = ', len(oddList), len(evenList))
    print('Excluding primes')
    return (oddList, evenList)

def listToCsv(myList, fileName):
    with open(fileName, 'w', newline='') as myfile:
        wr = writer(myfile, quoting=QUOTE_NONE, delimiter='\n', escapechar=' ')
        wr.writerow(myList)
        
def scatterPlotList(_list):
    coords = list(zip(*_list))        
    matplotlib.pyplot.scatter(coords[0], coords[1])
    matplotlib.pyplot.show()

main()
