import csv

def openDataFile(name):
    f = open(name, "r")
    return f

f1 = openDataFile("/Users/javanp/Documents/numbers.txt")

csvFile = csv.reader(f1)
for lines in csvFile:
    intList = [float(i) for i in lines]
    print(intList)
    intList.sort()
    print(intList)





