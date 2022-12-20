import difflib

def differ(file1, file2):    
    with open(f'{file1}') as file_1:
        file_1_text = file_1.readlines()
    
    with open(f'{file2}') as file_2:
        file_2_text = file_2.readlines()
    
    # Find and print the diff:
    for line in difflib.unified_diff(
            file_1_text, file_2_text, fromfile='file1.txt',
            tofile='file2.txt', lineterm=''):
        print(line)