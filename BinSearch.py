# Binary Search
import random

def binarySearch(array, search):
	last = len(array) -1
	for i in range(last):
		mid = i+last
		if array[mid] == search:
			return mid
		elif array[mid] < search:
			i-mid+1
		else:
			last-mid-1
	return -1

kl = []
for x in range(30):
	a = random.randint(0, 9)
	kl.append(a)
print(kl)
print (binarySearch(kl,0))