import redis
import string
import json

#from twilio.rest import TwilioRestClient
 

host,port = '155.41.116.171',6379

r = redis.Redis(host,port,db=0)
numPeople = 1


dict = {'Name':"Sean Smith", 'Party': 4, 'Phone': '6503158040'}
dict1 = {'Name':"Sean Smith", 'Party': 4, 'Phone': '6503158040'}
dict2 = {'Name':"Sean Smith", 'Party': 4, 'Phone': '6503158040'}
dict3 = {'Name':"Sean Smith", 'Party': 4, 'Phone': '6503158040'}
dict4 = {'Name':"Sean Smith", 'Party': 4, 'Phone': '6503158040'}

def add(d):
  x = json.dumps(d)
  r.lpush('party', x)
  global numPeople
  numPeople += 1
  
def getList():
  list = []
  for each in range(1, numPeople):
    d = r.lindex('party', each)
    dict1 = json.loads(d)
    list.append(dict1)
    #print(dict1['Name'])
  return list
    
def dequeue():
  x = r.lpop('party')
  dict1 = json.loads(x)
  sendMessage(dict1["Phone"], dict1["Name"])
  
def prettyPrint(list):
	for each in list:
	  print(each['Name']+'\t'+str(each['Party'])+'\t'+each['Phone'])
	  
	  
	  
def sendMessage(number, name):
  try:
    account_sid = "AC188d17e2092a0c9fc87b2bf289935edd"
    auth_token = "916ee78c2bac9b1dee98d730d599a791"
    client = TwilioRestClient(account_sid, auth_token)
    message = "Your table is ready " + name
    num = "+1"+number
    message = client.messages.create(to=num, from_="+16504168319",
                                     body=message)
  except twilio.TwilioRestException as e:
    print e
  
add(dict)

add(dict1)

add(dict2)

add(dict3)

add(dict4)
list  = getList()
prettyPrint(list)