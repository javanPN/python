import csv
import statistics
import functools
import operator

# def mean(list_of_nums):
#     total = 0
#     for num in list_of_nums:
#         total = total + num
#     return total / len(list_of_nums)

# def mode(list_of_nums):
#     max_count = (0, 0)
#     for num in list_of_nums:
#         occurences = list_of_nums.count(num)
#         if occurences > max_count[0]:
#             max_count = (occurences, num)
#     return max_count[1]

# def median(list_of_nums):
#     list_of_nums.sort()
#     if len(list_of_nums) % 2 != 0:
#         middle_index = int((len(list_of_nums - 1) / 2))
#         return list_of_nums[middle_index]
#     elif len(list_of_nums) % 2 == 0:
#         middle_index_1 = int(len(list_of_nums) / 2)
#         middle_index_2 =  int(len(list_of_nums) / 2) - 1
#         return mean([list_of_nums[middle_index_1], list_of_nums[middle_index_2]])

#f = open("/Users/javanp/Documents/numberstxt", "r")
def openDataFile(name):
    f = open(name, "r")
    return f

f1 = openDataFile("/Users/javanp/Documents/numbers.txt")
# f2 = openDataFile("/Users/javanp/Documents/numbers2.txt")

csvFile = csv.reader(f1)
allNumbers=[]
for lines in csvFile:
    # tmpList = []
    # for i in lines:
    #     if i == 'javan':
    #         i = 7
    #     tmpList.append(i)
    intList = [float(i) for i in lines]
    allNumbers.append(intList)
    print (intList)
    # print(mean(intList))
    # print(median(intList))
    # def flatten(l):
    #     return [item for sublist in l for item in sublist]


    # flat_list = [intList]
    # for sublist in intList:
    #     for item in flatten():
    #         flat_list.append(item)

    print("mean: % s " % statistics.mean(intList))
    print("median: % s " % statistics.median(intList))
    print("mode: % s " % statistics.mode(intList))
    # print(mode(intList))

# print(allNumbers)
flat_list = functools.reduce(operator.iconcat, allNumbers, [])
print(flat_list)

print("mean: % s " % statistics.mean(flat_list))
print("median: % s " % statistics.median(flat_list))
print("mode: % s " % statistics.mode(flat_list))

# numbers=[]
# print(median(numbers))
# print(mean(numbers))
# print(mode(numbers))