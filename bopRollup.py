import json
from pathlib import Path
import collections

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
  incumbentObj = {'incumbentTotal':incumbentTotal}
  gopObj = {'gop': gop}
  demObj = {'dem':dem}
  otherObj = {'other': other}
#   partyCount.append(incumbentObj)
#   partyCount.append(gopObj)
#   partyCount.append(demObj)
#   partyCount.append(otherObj)
  chamberObj ={'chamber':chamberName,'incubmentTotal':incumbentTotal, 'gop':gop, 'dem':dem, 'other':other}
  stateObj = {'state':stateName,  'chamberInfo':chamberObj}
  bopRollup.append(stateObj)
  newlist = sorted(bopRollup, key=lambda d: d['state'])
  print(newlist)
  combinedList = collections.defaultdict(list)
  for chamberInfo in newlist:
    combinedList[chamberInfo['state']].append(chamberInfo['chamberInfo'])
  newlist = [{'state': key, 'chamberInfo': value} for key, value in combinedList.items()]
with open(f'{path}bopRollup.json', 'w') as json_file:
    json.dump(newlist, json_file)