## This file loops through the list of states that is divided into two groups to spread the 
# requests against two api keys to prevent reaching the daily limit of API requests too quickly.

import getIncumbents 
import updateChambers
import config 

apiKeys = [
    f'&apikey={config.apikey1}',
    f'&apikey={config.apiKey2}']

print(f'\033[96mConfig Settings:\x1B[0m\n  \033[94mYear:\x1B[0m \033[93m{config.year}\x1B[0m\n  \033[94mawsFlag set to:\x1B[0m \033[93m{config.awsFlag}\x1B[0m')
if config.awsFlag == True:
    print(f'\033[94mFiles will be saved to S3 bucket:\x1B[0m \033[93m{config.s3Bucket}\x1B[0m')
else:
    print('  \033[94mFiles will \033[93mnot be uploaded to S3\x1B[0m')

for x in range(len(apiKeys)):
    apiKey = apiKeys[x]
    stateList = config.stateLists[x]
    getIncumbents.getIncumbents(apiKey,stateList)
updateChambers.updateChambers()
   