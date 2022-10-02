import requests
import json

# import time



chamberList = ["lower", "upper"]

mainList = []
houses = ["upper", "lower"]
    
path = '/Users/jdale/other-repos/ga-legislature/public/output/'

x = input("Enter State NAME: ")
state = x
y = input("Which chamber? (upper or lower): ")
chamber = y
getFirstPage = f'https://v3.openstates.org/people?jurisdiction={state}&org_classification={chamber}&page=1&per_page=50&apikey=f186a663-061d-462c-8364-f20e6f3594ce'
findPageCount = requests.get(getFirstPage).json()
page_count = findPageCount['pagination']['max_page']
for x in range(page_count):
    pageNum = f'page={x+1}'
    baseUrl= f'https://v3.openstates.org/people?jurisdiction={state}&org_classification={chamber}&page=1&per_page=50&apikey=f186a663-061d-462c-8364-f20e6f3594ce&{pageNum}'
    response = requests.get(baseUrl).json()
    personList = response['results']
    mainList = mainList + personList
with open(f'{path}{state}-{chamber}.json', 'w') as json_file:
    json.dump(mainList, json_file)
print(f'  *** Condragulations, your file {state}-{chamber} has been updated! ***  ')

