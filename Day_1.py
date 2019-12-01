#Advent of Code Day 1

#Part One
import math
def part1():
    fuel_need = 0
    def module (mass):
        x = (math.floor(int(mass) / 3)) - 2
        return x

    with open("./day1_input.txt", "r") as file:
        for line in file:
            value = module(line)
            fuel_need += value
        print(fuel_need)

#part 2
def part2():
    fuel_need = 0
    def new_module(mass):
        temp = 0
        while int(mass) > 0:
            x = (math.floor(int(mass)/3))-2
            if x <= 0:
                break
            else: temp = temp+x
            mass = x
        return temp
    with open("./day1_input.txt", "r") as file:
        for line in file:
            value = new_module(line)
            fuel_need += value
        print(fuel_need)

part1()
part2()