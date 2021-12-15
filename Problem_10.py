"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million
"""

n = 2000000
prime_array = [True for i in range(n)]

for i in range(2, int(len(prime_array) ** 0.5)):
	if prime_array[i] == True:
		x = 0
		k = 0
		for j in range(3, n):
			if j == i**2 + (x*k):
				prime_array[j] = False
				x +=1
				k = i

sum_of_prime = sum([i for i in range(n) if prime_array[i] == True and i != 0 and i != 1])

print("The sum of all prime number below two millions is : ", sum_of_prime)