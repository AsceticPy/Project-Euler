"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
a = 1
b = 2
c = 100
solved = False
print("a = ", a, " b = ", b, " c = ", c)
for a in range(1, 1000):
	for b in range(1, 1000):
		for c in range(1, 1000):
			if a < b < c:
				if a + b + c == 1000:
					if a**2 + b**2 == c**2:
						solved = True
						break
		if solved:
			break
	if solved:
		break
product = a*b*c
print("The product of only triplet who exists is : ", product)