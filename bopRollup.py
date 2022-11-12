import json
from pathlib import Path
import pprint

bopRollup = []
directory = './public/output/incumbents/'
path = './public/output/'



files = Path(directory).glob('*')
for file in files:
  f = open(file)  
  data = json.load(f)
  gop = 0
  dem = 0
  other = 0
  stateName = data[0]['jurisdiction']['name']
  chamberName = data[0]['current_role']['org_classification']
  partyCount = []
  for datum in data:
    party = datum['party']
    if party == 'Republican':
      gop += 1
    elif party == 'Democratic':
      dem += 1
    else:
      other += 1
  incumbentTotal = gop + dem + other
  gopObj = {'gop': gop}
  demObj = {'dem':dem}
  otherObj = {'other': other}
  partyCount.append(gopObj)
  partyCount.append(demObj)
  partyCount.append(otherObj)
#   print(incumbentTotal)
#   print(partyCount)
  stateObj = {'state':stateName, 'chamber':chamberName, 'totalIncumbents':incumbentTotal, 'partyCount':partyCount}
#   print(stateObj)
  bopRollup.append(stateObj)
  newlist = sorted(bopRollup, key=lambda d: d['state'])
  print(newlist)
with open(f'{path}bopRollup.json', 'w') as json_file:
    json.dump(newlist, json_file)