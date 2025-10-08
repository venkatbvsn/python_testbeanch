data=input('Enter text to write to the file: ')
data += '\n'
file_name = 'output.txt'
with open(file_name,'w') as file1:
    written_chars = file1.write(data)
    if written_chars > 0:
        print('Data successfully written to', file_name)

data=input('Enter additional text to append: ')
with open(file_name,'a') as file1:
    written_chars = file1.write(data)
    if written_chars > 0:
        print('Data successfully appended.')

with open(file_name,'r') as file1:
    lines=file1.readlines()
    print('Final content of', file_name, ':')
    for line in lines:
        print(line)