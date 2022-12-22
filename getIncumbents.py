# This file generates a list of incumbents for each chamber in each state. The api returns a 
# max of 50 per page so for many chambers/states, it loops through to collect all the pages 
# and then mushes them togther.

def getIncumbents(apiKey, stateList):
    import requests
    import json
    import time
    import datetime
    import config

    path = f'./{config.path}/incumbents/'
    
    mainList = []
    baseURL= 'https://v3.openstates.org/people?jurisdiction='

    for x in range(len(stateList)):
        state = stateList[x]
        stateString= state.replace(" ", "_")
        if state == 'Nebraska':  ## Nebraska is an edge case.  It has a single chamber legislature
            chamberList = ['legislature']
            classifier = 'classification'
        else:
            chamberList = ['lower','upper']
            classifier = 'org_classification'
        for y in range(len(chamberList)): ## loops through for each chamber
            print(f'\n** Initiating initial request for \033[93m{state} {chamberList[y]}\x1B[0m chamber in 20 seconds **')
            for i in range(20,0,-1):
                print(f"{i}", end=" \r", flush=True)
                time.sleep(1)
            chamber = chamberList[y]
            getFirstPage = f'{baseURL}{state}&{classifier}={chamber}&page=1&per_page=50{apiKey}'
            findPageCount = requests.get(getFirstPage).json()
            page_count = findPageCount['pagination']['max_page']
            personList = findPageCount['results']
            mainList = mainList + personList
            for z in range(page_count-1):
                print(f'Fetching next request for {state} {chamber} chamber in 10 seconds')
                for i in range(10,0,-1):
                    print(f"{i}", end=" \r", flush=True)
                    time.sleep(1)
                if page_count > 1:
                    pageNum = f'page={z+2}'
                    secondaryUrl= f'{baseURL}{state}&org_classification={chamber}&page=1&per_page=50{apiKey}&{pageNum}'
                    response = requests.get(secondaryUrl).json()
                    personList = response['results']
                    mainList = mainList + personList
                else:
                    pass
            now = datetime.datetime.now()
            newJson = {"timestamp":now.strftime("%m-%d-%Y %H:%M:%S"), 'incumbents': mainList}
            with open(f'{path}{stateString}-{chamber}.json', 'w') as json_file:
                json.dump(newJson, json_file)
            print(f'✅ \033[93m{state}-{chamber}\x1B[0m has been updated! ***  \n')
            mainList=[]

