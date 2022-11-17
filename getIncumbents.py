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
    'Florida'
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
# 'Wyoming'
]

apiKey= '&apikey=f186a663-061d-462c-8364-f20e6f3594ce'
baseURL= 'https://v3.openstates.org/people?jurisdiction='

    
path = './public/output/incumbents/'

for x in range(len(stateList)):
    state = stateList[x]
    stateString= state.replace(" ", "_")
    for y in range(len(chamberList)):
        time.sleep(20)
        chamber = chamberList[y]
        getFirstPage = f'{baseURL}{state}&org_classification={chamber}&page=1&per_page=50{apiKey}'
        findPageCount = requests.get(getFirstPage).json()
        page_count = findPageCount['pagination']['max_page']
        firstResponse = requests.get(getFirstPage).json()
        personList = firstResponse['results']
        for z in range(page_count-1):
            time.sleep(10)
            mainList = mainList + personList
            if page_count > 1:
                pageNum = f'page={z+2}'
                secondaryUrl= f'{baseURL}{state}&org_classification={chamber}&page=1&per_page=50{apiKey}&{pageNum}'
                response = requests.get(secondaryUrl).json()
                personList = response['results']
                mainList = mainList + personList
            else:
                 pass
        with open(f'{path}{stateString}-{chamber}.json', 'w') as json_file:
            json.dump(mainList, json_file)
        print(f'  *** Condragulations, your file {state}-{chamber} has been updated! ***  ')
        mainList=[]

