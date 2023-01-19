import secrets

apikey1 = f"{secrets.apikey1}"
apiKey2 = f"{secrets.apikey2}"


year = '2023' 
## Set this to the current year. The API doesn't provide historical data, 
# only current information for the legisatures. ## 

path = f'public/output/{year}'


awsFlag = False
## Set to True if you have an S3 bucket you would like to upload your files 
# to after they are created. You will need to have configured your machine/s3 
# bucket to allow for this before it will work.##  

s3Bucket = 'jrd-primary-public' 
## You will not have persmissions to upload to my bucket, 
# insert your configured bucket's name here if you wish. ##

stateLists = [['Hawaii'], ['Nebraska']] 
# ## This alternate statesList is for testing out code changes to ensure that 
# you haven't broken anything without having to loop through all 50 states.  ##

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

##This is the list of all 50 states. This list is separated into a list of two 
# lists to break them up to allow for the use of 2 api keys if you wish to prevent 
# exhaustion of your daily limits to the API as quickly as with using one APIkey. ##