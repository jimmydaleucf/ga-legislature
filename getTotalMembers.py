import requests
import json

import time

path = './public/output/'

stateList = ['Alabama',
'Alaska',
'Arizona']

# stateList =['Alabama',
# 'Alaska',
# 'Arizona',
# 'Arkansas',
# 'California',
# 'Colorado',
# 'Connecticut',
# 'Delaware',
# 'Florida',
# 'Georgia',
# 'Hawaii',
# 'Idaho',
# 'Illinois',
# 'Indiana',
# 'Iowa',
# 'Kansas',
# 'Kentucky',
# 'Louisiana',
# 'Maine',
# 'Maryland',
# 'Massachusetts',
# 'Michigan',
# 'Minnesota',
# 'Mississippi',
# 'Missouri',
# 'Montana',
# 'Nebraska',
# 'Nevada',
# 'New Hampshire',
# 'New Jersey',
# 'New Mexico',
# 'New York',
# 'North Carolina',
# 'North Dakota',
# 'Ohio',
# 'Oklahoma',
# 'Oregon',
# 'Pennsylvania',
# 'Rhode Island',
# 'South Carolina',
# 'South Dakota',
# 'Tennessee',
# 'Texas',
# 'Utah',
# 'Vermont',
# 'Virginia',
# 'Washington',
# 'West Virginia',
# 'Wisconsin',
# 'Wyoming']

output = []
# x = input("Enter State Postal Abbreviation: ")
# state = x
# y = input("Which chamber? (upper or lower): ")
# chamber = y

for x in range(len(stateList)):
    time.sleep(20)
    state = stateList[x]
    chamberInfo =  requests.get(f'https://v3.openstates.org/jurisdictions/{state}?include=organizations&apikey=f186a663-061d-462c-8364-f20e6f3594ce').json()
    organizations = chamberInfo['organizations']
    orgCount = len(organizations)
    chamberArray = []
    for x in range(orgCount):
        name =organizations[x]['name']
        districts = organizations[x]['districts']
        seats = len(districts)
        whichOne = organizations[x]['classification']        
        stateDictionary = {
            "org": name,
            "classification": whichOne,
            "totalSeats": seats,
        }
        chamberArray.append(stateDictionary)

    combined = {"state": state,
                "organizations":chamberArray}
    output.append(combined)
    print(f'********* {state} complete! ***********')
    with open(f'{path}legislatureDataFile.json', 'w') as json_file:
        json.dump(output, json_file)
print('your file has been created Jimmy!')