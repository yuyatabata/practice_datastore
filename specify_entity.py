from google.cloud import datastore

client = datastore.Client()

id = 1
key = client.key("media", id)
entity = client.get(key)
print(entity)