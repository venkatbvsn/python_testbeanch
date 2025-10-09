# ASSIGNMENT 2 Module 3 Task 1: Check if a Number is Even or Odd
a=int(input('Enter a number: '))

if ((a % 2 ) == 0):
    print(a, ' is an even number')
else:
    print(a, ' is an odd number')

# ASSIGNMENT 2 Module 3 Task 2: Sum of Integers from 1 to 50 Using a Loop
sum=0
for i in range(1, 51):
    sum +=i
print("The sum of numbers from 1 to 50 is: ", sum)