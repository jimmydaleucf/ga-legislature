import config
import  chamberGenerator
import  bopRollup
import os
import requests
import uploadFile
import json

year = config.year
awsFlag = config.awsFlag
bucketName = config.s3Bucket
path = config.path

def updateChambers():
    bopRollup.bopRollup()
    if awsFlag == True:
       file = requests.get(
        'https://jrd-primary-public.s3.amazonaws.com/bopRollup.json').json()
       os.chdir(f'./{path}/diagrams/')
    else:
         f = open(f'{path}/bopRollup.json')
         file = json.load(f)
         print(file)
         os.chdir(f'./{path}/diagrams/')
    states = file['states']
    for x in range(len(states)):
        stateName = states[x]['state']
        stateOrgs = states[x]['organizations']
        for y in range(len(stateOrgs)):
            chamber = stateOrgs[y]['classification']
            # chamberTotal = stateOrgs[y]['totalSeats']
            filename = f'{stateName}-{chamber}-diagram.svg'
            dem = stateOrgs[y]['dem']
            gop = stateOrgs[y]['gop']
            other = stateOrgs[y]['other']
            # totalIncumbents = dem + gop + other
            vacant = stateOrgs[y]['vacant']
            input_list = {
                'parties': [
                    {
                        'name': 'Democrat',
                        'nb_seats': int(dem),
                        'color': '#4165d2',
                        'border_size': 0,
                        'border_color': '#000000'
                    },
                    {
                        'name': 'Other',
                        'nb_seats': int(other),
                        'color': '#e3bb1c',
                        'border_size': 0,
                        'border_color': '#000000'
                    },
                    {
                        'name': 'Vacant',
                        'nb_seats': int(vacant),
                        'color': '#808080',
                        'border_size': 0,
                        'border_color': '#000000'
                    },
                    {
                        'name': 'Republican',
                        'nb_seats': int(gop),
                        'color': '#dc3d3d',
                        'border_size': 0,
                        'border_color': '#000000'
                    }
                ],
                'denser_rows': False
            }
            if awsFlag == True:
                chamberGenerator.chamberGenerator(input_list, filename)
                uploadFile.upload_file(f'{filename}', f'{bucketName}', f'{year}/hemicycles/{filename}')
            else:
                chamberGenerator.chamberGenerator(input_list, filename)


            

