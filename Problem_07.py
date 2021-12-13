"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def prime_number(n: int) -> bool:
		prime = True
		for i in range(2, n):
			if n%i == 0:
				prime = False
				break
		return prime

continue0 = True
i = 2 
x = 1 
while continue0:
	if prime_number(i):
		if x == 10001:
			break
		x = x + 1
	i += 1

print("The 10 001st prime number is : ", i)

