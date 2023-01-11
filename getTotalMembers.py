# This file creates a rollup of the total members of each chamber in each state and compiles it into a single file.
# It does not have to be run more than once as the total number of seats in a legilsative body do not change.  If any
# state were to change the number of seats in one of their chambers, simply running this once would update this rollup.


import requests
import json
import time
import datetime
import uploadFile
import config

path = f'./{config.path}/'

apiKey = config.apikey1

# stateList = [
# 'Alabama', 'Alaska']

stateList = ['Alabama',
             'Alaska',
             'Arizona',
             'Arkansas',
             'California',
             'Colorado',
             'Connecticut',
             'Delaware',
             'Florida',
             'Georgia',
             'Hawaii',
             'Idaho',
             'Illinois',
             'Indiana',
             'Iowa',
             'Kansas',
             'Kentucky',
             'Louisiana',
             'Maine',
             'Maryland',
             'Massachusetts',
             'Michigan',
             'Minnesota',
             'Mississippi',
             'Missouri',
             'Montana',
             'Nebraska',
             'Nevada',
             'New Hampshire',
             'New Jersey',
             'New Mexico',
             'New York',
             'North Carolina',
             'North Dakota',
             'Ohio',
             'Oklahoma',
             'Oregon',
             'Pennsylvania',
             'Rhode Island',
             'South Carolina',
             'South Dakota',
             'Tennessee',
             'Texas',
             'Utah',
             'Vermont',
             'Virginia',
             'Washington',
             'West Virginia',
             'Wisconsin',
             'Wyoming']

output = []


for x in range(len(stateList)):
    print(f'\n******* Initiating request for {stateList[x]} *********')
    # time.sleep(20)
    for i in range(20, 0, -1):
        print(f"{i}", end=" \r", flush=True)
        time.sleep(1)
    state = stateList[x]
    chamberInfo = requests.get(
        f'https://v3.openstates.org/jurisdictions/{state}?include=organizations&apikey={apiKey}').json()
    organizations = chamberInfo['organizations']
    orgCount = len(organizations)
    chamberArray = []
    for x in range(orgCount):
        seats = 0
        name = organizations[x]['name']
        districts = organizations[x]['districts']
        # print(districts)
        for z in range(len(districts)):
            maxMembers = districts[z]['maximum_memberships']
            seats = seats + maxMembers
        print(f'{name}: {seats} seats')
        whichOne = organizations[x]['classification']
        stateDictionary = {
            "org": name,
            "classification": whichOne,
            "totalSeats": seats,
        }
        chamberArray.append(stateDictionary)
    combined = {"state": state,
                "organizations": chamberArray}
    output.append(combined)
    print(f'\n ✅ Request information from {state} complete!')
now = datetime.datetime.now()
ChambersTotal = {"timestamp": now.strftime(
    "%m-%d-%Y %H:%M:%S"), 'states': output}
with open(f'{path}ChambersTotal.json', 'w') as json_file:
    json.dump(ChambersTotal, json_file)
print('\n ✅ Your file \033[93mChambersTotal.json\x1B[0m has been created Jimmy!')
uploadFile.upload_file(f'{path}ChambersTotal.json', 'jrd-primary-public')
print('Your \033[93mChambersTotal.json\x1B[0m file has been updloaded to S3 bucket \033[94m"jrd-primary-public"\x1B[0m')
