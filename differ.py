import difflib

print("what is the first file?")
file1 = input()
print("what is the second file?")
file2 = input()

with open(f'{file1}') as file_1:
    file_1_text = file_1.readlines()

with open(f'{file2}') as file_2:
    file_2_text = file_2.readlines()

# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='file1.txt',
        tofile='file2.txt', lineterm=''):
    print(line)

