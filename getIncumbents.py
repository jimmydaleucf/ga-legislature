def getIncumbents(apiKey, stateList):
    import requests
    import json
    import time
    path = './public/output/incumbents/'
    
    mainList = []
    baseURL= 'https://v3.openstates.org/people?jurisdiction='

    for x in range(len(stateList)):
        state = stateList[x]
        stateString= state.replace(" ", "_")
        if state == 'Nebraska':
            chamberList = ['legislature']
            classifier = 'classification'
        else:
            chamberList = ['lower','upper']
            classifier = 'org_classification'
        for y in range(len(chamberList)):
            print(f'Initiating inital request for {state} {chamberList[y]} chamber in 20 seconds')
            # time.sleep(20)
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
                    # print(secondaryUrl)
                    response = requests.get(secondaryUrl).json()
                    # print(response)
                    personList = response['results']
                    mainList = mainList + personList
                else:
                    pass
            with open(f'{path}{stateString}-{chamber}.json', 'w') as json_file:
                json.dump(mainList, json_file)
            print(f'/n  *** Condragulations, your file {state}-{chamber} has been updated! ***  /n')
            mainList=[]

