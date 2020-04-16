from google.cloud import datastore

client = datastore.Client()


key = client.key("Task")
entity = datastore.Entity(key)
entity['description'] = "Buy milk"
entity['username'] = "Qiita"
client.put(entity)