#AOC Day2

import math
import copy

def Convert(string):
    li = list(string.split(","))
    return li
with open("./day2_input.txt", "r") as file:
   for line in file:
      data=(Convert(line))
data1 = [int(i) for i in data]
newdata = copy.deepcopy(data1)
print(newdata[0:4])
def part1():
    posit = 0
    data1[1]=12
    data1[2]=2
    print(data1[0:4])
    while data1[posit] != 99:
        if data1[posit] == 1:
            temp1 = data1[posit+1]
            temp2 = data1[posit+2]
            temp3 = data1[posit+3]
            value = data1[temp1]+data1[temp2]
            data1[temp3] = value
            posit += 4
        else:
            temp1 = data1[posit + 1]
            temp2 = data1[posit + 2]
            temp3 = data1[posit + 3]
            value = data1[temp1] * data1[temp2]
            data1[temp3] = value
            posit += 4

def part2():
    noun = [x for x in range(100)]
    verb = [x for x in range(100)]
    for i in noun:
        for j in verb:
            data1 = copy.deepcopy(newdata)
            posit=0
            data1[1]=i
            data1[2]=j
            while data1[posit] != 99:
                if data1[posit] == 1:
                    temp1 = data1[posit+1]
                    temp2 = data1[posit+2]
                    temp3 = data1[posit+3]
                    value = data1[temp1]+data1[temp2]
                    data1[temp3] = value
                    posit += 4
                else:
                    temp1 = data1[posit + 1]
                    temp2 = data1[posit + 2]
                    temp3 = data1[posit + 3]
                    value = data1[temp1] * data1[temp2]
                    data1[temp3] = value
                    posit += 4
            if data1[0] == 19690720:
                print (i)
                print (j)
                print (100*i+j)
                break

part1()
part2()
