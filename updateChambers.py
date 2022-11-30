import chamberGenerator
import bopRollup
import json
import os




f = open('public/output/bopRollup.json')
file = json.load(f)
os.chdir('./public/diagrams/')

states = file['states']
for x in range(len(states)):
    stateName = states[x]['state']
    stateOrgs =states[x]['organizations']
    for y in range(len(stateOrgs)):
        chamberName = stateOrgs[y]['org']
        chamberTotal =stateOrgs[y]['totalSeats']
        filename = f'{stateName}-{chamberName}-diagram.svg'
        dem = stateOrgs[y]['dem']
        gop = stateOrgs[y]['gop']
        other = stateOrgs[y]['other']
        input_list = {
            'parties': [
                {
                    'name': 'Democrat',
                    'nb_seats':int(dem),
                    'color': '#4165d2' ,
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
                    'name': 'Republican',
                    'nb_seats': int(gop),
                    'color': '#dc3d3d' ,
                    'border_size': 0,
                    'border_color': '#000000'
                }
            ],
            'denser_rows': False
        }
        chamberGenerator.chamberGenerator(input_list, filename)




# chamberGenerator.chamberGenerator(input_list)