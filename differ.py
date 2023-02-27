import json
import sys

from termcolor import colored


def differ(**newJson):
    file1 = open('public/output/2023/bopRollup.json')
    json1= json.load(file1)
    # file2= open('public/output/2023/bopRollup.json')
    # json2= json.load(file2)
    json2 = newJson

    changed = []
    unChanged = []



    # mode = input('Which mode?\n1. Changed \n2. Not Changed\nEnter number:')

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

    # if mode == '1':
    print('Diff results: The following states/chambers are different from the original file:')

    for state in changed:
        text = colored(state, 'green')
        print(text)
# elif mode == '2':
    print('Diff results: The following states/chambers have NOT changed from the original file:')
    for state in unChanged:
        text = colored(state, 'red')
        print(text)
# else:
    # print('please enter either 1 or 2')



