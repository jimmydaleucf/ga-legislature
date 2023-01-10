# This file loops through the list of states that is divided into two groups to spread the
# requests against two api keys to prevent reaching the daily limit of API requests too quickly.

import dataProcessing.getIncumbents as getIncumbents
import updateChambers
import dataProcessing.config as config

firstKey = config.apikey1
secondKey = config.apiKey2

apiKeys = [
    f'&apikey={firstKey}',
    f'&apikey={secondKey}']

# stateLists  =[[
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
# 'Nebraska',
# 'Nevada',
# 'New Hampshire'],[
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
# 'Wyoming']]

# stateLists = [['Nebraska']]

stateLists = [['Hawaii'], ['Nebraska']]


for x in range(len(apiKeys)):
    apiKey = apiKeys[x]
    stateList = stateLists[x]
    getIncumbents.getIncumbents(apiKey, stateList)
updateChambers.updateChambers()
