## This file loops through the list of states that is divided into two groups to spread the 
# requests against two api keys to prevent reaching the daily limit of API requests too quickly.

import dataProcessing.getIncumbents as getIncumbents
import updateChambers
import dataProcessing.config as config

apiKeys = [
    f'&apikey={config.apikey1}',
    f'&apikey={config.apiKey2}']

for x in range(len(apiKeys)):
    apiKey = apiKeys[x]
    stateList = config.stateLists[x]
    getIncumbents.getIncumbents(apiKey,stateList)
updateChambers.updateChambers()
   