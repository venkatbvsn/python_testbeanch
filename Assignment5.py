# ASSIGNMENT 5 Module 6 Task 1: Create a Dictionary of Student Marks
student_dictionary={}
for i in range(3):
    name=input('Enter the student\'s name: ')
    marks=int(input('{}\'s marks: '.format(name)))
    student_dictionary[name]=marks

name=input('Enter the student\'s name to be found: ')
if name in student_dictionary:
    print('Student found. He got {} marks.'.format(student_dictionary[name]))
else:
    print('Student not found')


# ASSIGNMENT 5 Module 6 Task 2: Demonstrate List Slicing
l1=[i for i in range(1,11)]
print('Original list: ', l1)
l2=l1[:5]
print('Extracted first five elements: ', l2)
l2.reverse()
print('Reversed extracted elements: ', l2)