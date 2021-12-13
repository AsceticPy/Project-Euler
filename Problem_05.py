"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
n = 0

while True:
	n = n + 1
	number_div = 0
	smallest = False
	if n%10 == 0 and n%3 == 0:
		for i in range(1, 20):
			if n%i == 0:
				smallest = True
				number_div += 1
			else:
				smallest = False
				break
	if smallest:
		break
print("The smallest number who can be divisible by all of the numbers from 1 to 20 is : ", n)