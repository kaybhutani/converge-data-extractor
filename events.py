import pymongo
import config
names={
    "groove": "GROOVE",
    "inquizzitive": "INQUIZZITIVE",
    "rihaa": "RIHAA",
    "mehfil": "MEHFIL",
    "advaya": "ADVAYA",
    "sabrang": "SABRANG",
    "ppr": "PLAY PAUSE REWIND",
    "fts": "FLUTTER THE SHUTTER",
    "poise": "POISE",
    "mconv": "MR and MS CONVERGE",
"adsmd":"Adi Shankaracharya Memorial Debate","jzbaat":"Jazbaat- The Open Mic Show",
    "acst":"ACOUSTICA",
    "crsd":"CRUSADE",
"marathon":"Marathon",
"algoflux":"AlgoFlux",
"codft":"CodeFight",
"rpdfire":"RapidFire",
"bdmntnboys":"Badminton Boys",
"bdmntngirls":"Badminton Girls",
"vllyballb":"Volley Ball Boys",
 "vllyballg":"Volley Ball Girls",
"football":"Football",
"tt":"Table Tennis",
"crckt":"CRICEKT",
    "bbb":"Basketball Boys",
    "bbg":"Basketball Girls",
    "chess":"Chess"
  }
heads={
    "groove": "pranav3nov@gmail.com",
    "inquizzitive": "b.dubey1111@gmail.com",
    "rihaa": "abhivyakti128@gmail.com",
    "mehfil": "abhivyakti128@gmail.com",
    "advaya": "parthsethi1998@gmail.com",
    "sabrang": "parthsethi1998@gmail.com",
    "ppr": "cinekala.jiit128@gmail.com",
    "fts": "auraphotography.128@gmail.com",
    "poise": "goyal.jahanvi@gmail.com",
    "mconv": "goyal.jahanvi@gmail.com",
"adsmd":"princebest3@rediffmail.com","jzbaat":"princebest3@rediffmail.com",
    "acst":"fortissimojiit128@gmail.com",
    "crsd":"fortissimojiit128@gmail.com",
 "marathon":"ashitagoel10@gmail.com",
 "algoflux":"rohanmukhija10@gmail.com",
    "codft":"rohanmukhija10@gmail.com",
"rpdfire":"rohanmukhija10@gmail.com",
"bdmntnboys":"kartikeya2998@gmail.com",
"bdmntngirls":"kartikeya2998@gmail.com",
"vllyballb":"gauravjiit4@gmail.com",
"vllyballg":"gauravjiit4@gmail.com",
"football":"utkarsh4419@yahoo.com",
"tt":"shivamkhurana1998@gmail.com",
"crckt":"toyeshsingh32@gmail.com",
"bbb":"amoghmisra27@gmail.com",
"bbg":"amoghmisra27@gmail.com",
"chess":"nayanraj911@gmail.com"
  }

def getEventsOfHead(email):
  temp=[]
  for i in heads:
    if(heads[i]==email):
      temp.append(i)
  return temp

def getDatabase(events):
  client = pymongo.MongoClient(config.MONGODB_URI, connectTimeoutMS=30000)
  db = client.converge2020
  col = db["registrations"]
  finalDataOfHead = {} #json of event with eventsReg data
  for event in events:
    eventsReg = [] #array of json user data
    for i in col.find({'eventName': event}):
      print(i)
      eventsReg.append(i['userData'])
    finalDataOfHead[getFullEventName(event)] = eventsReg
  return finalDataOfHead

def getFullEventName(event):
  return names[event]
