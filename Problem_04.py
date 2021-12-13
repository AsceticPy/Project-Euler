"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

biggest_number = 0

for i in range(999):
	for n in range(999):
		number = i*n
		if str(number) == str(number)[::-1]:
			if number > biggest_number:
				biggest_number = number
print(biggest_number)