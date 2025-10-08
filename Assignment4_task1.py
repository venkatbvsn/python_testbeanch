file_name = 'sample.txt'
try:
    with open(file_name,'r') as file1:
        lines = file1.readlines()
        i=1
        for line in lines:
            print('line', i , ':', line)
            i+=1
except FileNotFoundError:
    print('Error: The file ', file_name, 'was not found.')