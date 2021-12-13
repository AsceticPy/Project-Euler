"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
sum_of_the_square = sum((i**2 for i in range(1, 101)))
square_of_the_sum = sum(i for i in range(1, 101))**2
difference = square_of_the_sum - sum_of_the_square
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is : ", difference)