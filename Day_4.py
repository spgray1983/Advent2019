#!/usr/bin/env python3

#Day 4
import math

start = 158126
end = 624574
count = 0
count2 = 0

def check_double(value):
	value = str(value)
	if value[0]==value[1]:
		return True
	elif value[1] == value[2]:
		return True
	elif value[2] == value[3]:
		return True
	elif value[3] == value[4]:
		return True
	elif value[4] == value[5]:
		return True
	else: return False

def check_inc(value):
	value = str(value)
	if (value[0] <= value[1] and value[1] <= value[2] and value[2] <= value[3] and value[3] <= value[4] and value[4] <= value[5]):
		return True
	else: return False

def new_check(value):
	value = str(value)
	if value[0] == value[1] == value[2] == value[3]:
		return True
	elif value[1] == value[2] == value[3] == value[4]:
		return True
	elif value[2] == value[3] == value[4] == value[5]:
		return True
	elif value[0]==value[1] and value[1]<value[2] and value[2]==value[3]:
		return True
	elif value[0]!= value[1] and value[1]==value[2] and value[2]<value[3] and value[3]==value[4]:
		return True
	elif value[2]==value[3] and value[3]<value[4] and value[4]==value[5]:
		return True
	elif value[0]==value[1] and value[1]<value[2] and value[2]==value[3] and value[3]<=value[4] and value[4]==value[5]:
		return True
	elif value[0] == value[1] == value[2] == value[3] == value[4] == value [5]:
		return True
	else: return False

#Count returns part 1 answer AND Count2 is part 2
while start <= end:
	if (check_double(start) == True and check_inc(start) == True and new_check(start)==True):
		count2 +=1
		count +=1
		start +=1
	elif (check_double(start) == True and check_inc(start) == True):
		count +=1
		start +=1

	else: start +=1
print (count)
print (count2)
