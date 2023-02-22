# import difflib

# print("what is the first file?")
# file1 = input()
# print("what is the second file?")
# file2 = input()

# with open(f'{file1}') as file_1:
#     file_1_text = file_1.readlines()

# with open(f'{file2}') as file_2:
#     file_2_text = file_2.readlines()

# # Find and print the diff:
# for line in difflib.unified_diff(
#         file_1_text, file_2_text, fromfile='file1.txt',
#         tofile='file2.txt', lineterm=''):
#     print(line)
import json
import sys

from termcolor import colored

file1 = open('public/output/2022/bopRollup.json')
json1= json.load(file1)
file2= open('public/output/2023/bopRollup.json')
json2= json.load(file2)

changed = []
unChanged = []



userInput = input('Which mode?\n1. Changed \n2. Not Changed\nEnter number:')

states1 = json1['states']
states2 = json2['states']
for x in range(len(states1)):
    name1 = states1[x]['state']
    name2 = states2[x]['state']
    orgs1 = states1[x]['organizations']
    orgs2 = states2[x]['organizations']
    for x in range(len(orgs1)):
        chamber1 = orgs1[x]['org']
        if orgs1 == orgs2:
            data = f'{name1} {chamber1}'
            unChanged.append(data)
        else:
            data = f'{name1} {chamber1}'
            changed.append(data)
        # print(f'Changes detected in {name1} {chamber1}')
print('Diff results: The following states/chambers are different from the original file:')
for state in changed:
    text = colored(state, 'yellow')
    print(text)
print('Diff results: The following states/chambers have NOT changed from the original file:')
for state in unChanged:
    text = colored(state, 'green')
    print(text)
