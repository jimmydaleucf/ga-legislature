import getIncumbents

apiKeys= [
    # '&apikey=f186a663-061d-462c-8364-f20e6f3594ce', 
    '&apikey=047dc17e-0268-4b55-9eab-3ae74457228d']
stateList =[
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
    'Hawaii'
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
    # 'New York',
    # 'Florida'
    # 'North Carolina',
    # 'North Dakota'
    ]

apiKey = '&apikey=047dc17e-0268-4b55-9eab-3ae74457228d'
stateList2 = [
    'Ohio'
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
# for x in apiKeys:
#     apiKey = x
#     print(apiKey)
#     print(stateList)
getIncumbents.getIncumbents(apiKey,stateList)
   