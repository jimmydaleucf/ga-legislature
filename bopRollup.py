
# This file takes all the individual files of incumbets saved in /public/output/incumbents/ 
# and creates a rollup by counting all the repubs, the dems, and the others.  It creates a lightweight
# rollup by state.  
import json
from pathlib import Path
import collections

bopRollup = []
directory = './public/output/incumbents/'
directoryTwo = 'public/output/ChambersTotal.json'
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
    orgClass = datum['current_role']['org_classification']
    if orgClass != 'executive':
      if party == 'Republican':
        gop += 1
      elif party == 'Democratic':
        dem += 1
      else:
        other += 1
    else:
      pass
  incumbentTotal = gop + dem + other
  incumbentObj = {'incumbentTotal':incumbentTotal}
  gopObj = {'gop': gop}
  demObj = {'dem':dem}
  otherObj = {'other': other}
  chamberObj ={'classification':chamberName,'incubmentTotal':incumbentTotal, 'gop':gop, 'dem':dem, 'other':other}
  stateObj = {'state':stateName,  'organizations':[chamberObj]}
  bopRollup.append(stateObj)
combinedTotal = open(directoryTwo)
combinedTotalObj = json.load(combinedTotal)
mergedList = bopRollup + combinedTotalObj
newlist = sorted(mergedList, key=lambda d: d['state'])
combinedList = collections.defaultdict(list)
for organizations in newlist:
  combinedList[organizations['state']].extend(organizations['organizations'])
newlist = [{'state': key, 'organizations': value} for key, value in combinedList.items()]
for state in newlist:
    upperChamber = []
    lowerChamber = []
    orgs = state['organizations']
    container = []
    for org in orgs:
        if org['classification'] == 'upper':
            upperChamber.append(org)
        elif org['classification'] == 'lower':
            lowerChamber.append(org)
        elif org['classification'] == 'legislature' and state['state']== 'Nebraska':
            upperChamber.append(org)
    if state['state'] != "Nebraska":
        newThing = upperChamber[0] | upperChamber[1]
        newThing2 = lowerChamber[0] | lowerChamber[1]
        container.append(newThing2)
    else:
        newThing = upperChamber[0] | upperChamber[1]
    container.append(newThing)
    state['organizations'] = container
with open(f'{path}bopRollup.json', 'w') as json_file:
    json.dump(newlist, json_file)
    print('\n✅ Your "bopRollup.json" file updated!\n')