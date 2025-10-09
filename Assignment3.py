# ASSIGNMENT 3 Module 4 Task 1: Calculate Factorial Using a Function
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

num=int(input('Enter a number: '))
ans=factorial(num)
print('Factorial of ', num , 'is: ', ans)

# ASSIGNMENT 3 Module 4 Task 2: Using the Math Module for Calculations
import math
num = int(input('Enter a number: '))
print('Square root: ',math.sqrt(num))
print('Logarithm: ',math.log(num))
print('Sine: ',math.sin(num))