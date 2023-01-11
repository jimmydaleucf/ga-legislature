## This file loops through the list of states that is divided into two groups to spread the 
# requests against two api keys to prevent reaching the daily limit of API requests too quickly.

import getIncumbents 
import updateChambers
import config 

apiKeys = [
    f'&apikey={config.apikey1}',
    f'&apikey={config.apiKey2}']

for x in range(len(apiKeys)):
    apiKey = apiKeys[x]
    stateList = config.stateLists[x]
    print(stateList)
    getIncumbents.getIncumbents(apiKey,stateList)
updateChambers.updateChambers()
   