from google.cloud import datastore

client = datastore.Client()

query = client.query(kind="Task")
query.add_filter("username", "=", "Qiita")
query.order=["username"]

list(query.fetch())

# [<Entity('Task', 5634161670881280) {'username': 'Qiita', 'description': 'Buy milk'}>]
