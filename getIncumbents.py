import requests
import json

import time



chamberList = ["lower", "upper"]

mainList = []

# stateList = [
# 'Alabama', 
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
# 'Nevada',
# 'New Hampshire',
# 'New Jersey',
# 'New Mexico',
# 'New York'
# ]

stateList =[
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
'Vermont',
'Virginia',
'Washington',
'West Virginia',
'Wisconsin',
'Wyoming'
]


    
path = './public/output/incumbents/'

for x in range(len(stateList)):
    state = stateList[x]
    stateString= state.replace(" ", "_")
    for y in range(len(chamberList)):
        time.sleep(20)
        chamber = chamberList[y]
        getFirstPage = f'https://v3.openstates.org/people?jurisdiction={state}&org_classification={chamber}&page=1&per_page=50&apikey=f186a663-061d-462c-8364-f20e6f3594ce'
        findPageCount = requests.get(getFirstPage).json()
        page_count = findPageCount['pagination']['max_page']
        for z in range(page_count):
            time.sleep(10)
            pageNum = f'page={z+1}'
            baseUrl= f'https://v3.openstates.org/people?jurisdiction={state}&org_classification={chamber}&page=1&per_page=50&apikey=f186a663-061d-462c-8364-f20e6f3594ce&{pageNum}'
            response = requests.get(baseUrl).json()
            personList = response['results']
            mainList = mainList + personList
        with open(f'{path}{stateString}-{chamber}.json', 'w') as json_file:
            json.dump(mainList, json_file)
        print(f'  *** Condragulations, your file {state}-{chamber} has been updated! ***  ')
        mainList=[]

