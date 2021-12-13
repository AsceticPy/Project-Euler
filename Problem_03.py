"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import math 

number = 600851475143

while number%2 == 0:
	number /= 2
	print("2", end = " ")

for n in range(3,int(math.sqrt(number))+1,2):
	while number%n ==0:
		number /= n
		print(n, end = " ")
if number > 2:
	print(number)
