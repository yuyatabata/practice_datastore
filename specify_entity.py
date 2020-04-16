from google.cloud import datastore

client = datastore.Client()

id = 5634161670881280
key = client.key("Task", id)
entity = client.get(key)
print(entity)