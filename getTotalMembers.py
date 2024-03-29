# This file creates a rollup of the total seats of each chamber in each state and compiles it into a single file.
# It does not have to be run more than once as the total number of seats in a legislative body do not change.  If any
# states were to change the number of seats in one of their chambers, simply running this once would update this rollup.


import requests
import json
import time
import datetime
import uploadFile
import config
import os

path = f'public/output/'

apiKey = config.apikey1
bucketName = config.s3Bucket
awsFlag = config.awsFlag
year = config.year

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
check_folder = os.path.isdir('/public/output/2023/')
with open(f'{path}ChambersTotal.json', 'w') as json_file:
    json.dump(ChambersTotal, json_file)
if awsFlag == True:
    print('\n ✅ Your file \033[93mChambersTotal.json\x1B[0m has been created Jimmy!')
    uploadFile.upload_file(f'{path}ChambersTotal.json', f'{bucketName}')
    print(f'Your \033[93mChambersTotal.json\x1B[0m file has been uploaded to S3 bucket \033[94m"{bucketName}"\x1B[0m')
else:
    print('\n ✅ Your file \033[93mChambersTotal.json\x1B[0m has been created Jimmy!')
   
