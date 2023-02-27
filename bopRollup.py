
  # This file takes all the individual files of incumbents saved in /public/output/incumbents/ 
  # and creates a rollup by counting all the repubs, the dems, and the others.  It creates a lightweight
  # rollup by state.  
def bopRollup():
  import json
  from pathlib import Path
  import collections
  import datetime
  import config
  import uploadFile
  import differ

  bopRollup = []
  
  path = config.path
  directory = f'./{path}/incumbents/'
  directoryTwo = f'public/output/ChambersTotal.json'
  year = config.year
  awsFlag = config.awsFlag
  bucketName = config.s3Bucket

  nationalDem = 0
  nationalGOP = 0
  nationalOther = 0
  nationalVacant = 0
  nationalTotalSeats = 0
  nationalincumbentTotal = 0
  combinedTotal = open(directoryTwo)
  files = Path(directory).glob('*')
  for file in files:
    f = open(file)  
    datafile = json.load(f)
    data = datafile['incumbents']
    gop = 0
    dem = 0
    other = 0
    stateName = data[0]['jurisdiction']['name']
    chamberName = data[0]['current_role']['org_classification'] 
    for datum in data:
      party = datum['party']
      orgClass = datum['current_role']['org_classification']
      if orgClass != 'executive':
        if 'Republican' in party:
          gop += 1
          nationalGOP += 1
        elif 'Democratic' in party: 
          dem += 1
          nationalDem += 1
        else:
          other += 1
          nationalOther += 1
      else:
        pass
    incumbentTotal = gop + dem + other
    nationalincumbentTotal = nationalincumbentTotal + incumbentTotal
    chamberObj ={'classification':chamberName,'incubmentTotal':incumbentTotal, 'gop':gop, 'dem':dem, 'other':other}
    stateObj = {'state':stateName,  'organizations':[chamberObj]}
    bopRollup.append(stateObj)
  ChambersTotal = json.load(combinedTotal)
  combinedTotalObj = ChambersTotal['states']
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
      for chamber in container:
        totalSeats = chamber['totalSeats']
        nationalTotalSeats = nationalTotalSeats + totalSeats
        vacant = totalSeats-chamber['incubmentTotal']
        nationalVacant = nationalVacant + vacant
        chamber.update({"vacant":vacant})
      state['organizations'] = container      
  nationalRollup = { "state": "US", "organizations": [{
          "classification": "National",
          "incubmentTotal": nationalincumbentTotal,
          "gop": nationalGOP,
          "dem": nationalDem,
          "other": nationalOther,
          "org": "National",
          "totalSeats": nationalTotalSeats,
          "vacant": nationalVacant
        }]}
  newlist.append(nationalRollup)
  now = datetime.datetime.now()
  newJson = {"timestamp":now.strftime("%m-%d-%Y %H:%M:%S"), "year":f"{year}",  'states':newlist}
  differ.differ(**newJson)
  with open(f'{path}/bopRollup.json', 'w') as json_file:
      json.dump(newJson, json_file)
  if awsFlag == True:
    print('\n✅ Your \033[93mbopRollup.json\x1B[0m file updated!\n')
    uploadFile.upload_file(f'{path}/bopRollup.json', f'{bucketName}', f'{year}/bopRollup.json')
    print(f'Your \033[93mbopRollup.json\x1B[0m file has been updloaded to S3 bucket \033[94m"{bucketName}"\x1B[0m')
  else:
    print('\n✅ Your \033[93mbopRollup.json\x1B[0m file updated!\n')


bopRollup()