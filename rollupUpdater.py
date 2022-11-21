import getIncumbents

apiKeys= [
    '&apikey=f186a663-061d-462c-8364-f20e6f3594ce'] 
    # '&apikey=047dc17e-0268-4b55-9eab-3ae74457228d']
# stateLists  =[[
#     'Ohio',
#     'Oklahoma',
#     'Oregon',
#     'Pennsylvania',
#     'Rhode Island',
#     'South Carolina',
#     'South Dakota',
#     'Tennessee',
#     'Texas',
#     'Utah',
#     'Vermont',
#     'Virginia',
#     'Washington',
#     'West Virginia',
#     'Wisconsin',
#     'Wyoming'
#     ],[
#     'Alabama', 
#     'Alaska',
#     'Arizona',
#     'Arkansas',
#     'California',
#     'Colorado',
#     'Connecticut',
#     'Delaware',
#     'Florida',
#     'Georgia',
#     'Hawaii'
#     'Idaho',
#     'Illinois',
#     'Indiana',
#     'Iowa',
#     'Kansas',
#     'Kentucky',
#     'Louisiana',
#     'Maine',
#     'Maryland',
#     'Massachusetts',
#     'Michigan',
#     'Minnesota',
#     'Mississippi',
#     'Missouri',
#     'Montana',
#     'Nevada',
#     'New Hampshire',
#     'New Jersey',
#     'New Mexico',
#     'New York',
#     'Florida'
#     'North Carolina',
#     'North Dakota'
#     ]]

stateLists = [['Nebraska']]

stateLists = [['Hawaii', 'Nebraska']]
# apiKey = '&apikey=047dc17e-0268-4b55-9eab-3ae74457228d'

for x in range(len(apiKeys)):
    apiKey = apiKeys[x]
    stateList = stateLists[x]
    getIncumbents.getIncumbents(apiKey,stateList)
   