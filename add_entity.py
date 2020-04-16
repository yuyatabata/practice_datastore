from google.cloud import datastore

client = datastore.Client()

key = client.key("Task")
entityA = datastore.Entity(key)
dataA = dict()
dataA['username'] = 'A-san'
dataA['description'] = 'Help B-san'
entityA.update(dataA)

entityB = datastore.Entity(key)
dataB = dict()
dataB['username'] = 'B-san'
dataB['description'] = 'Buy beer'
entityB.update(dataB)

client.put_multi([entityA,entityB])