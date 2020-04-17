from google.cloud import datastore

client = datastore.Client()

query = client.query(kind="media_table_structure")
# query.add_filter("username", "=", "Qiita")
# query.order=["username"]



print(list(query.fetch()))

# [<Entity('Task', 5634161670881280) {'username': 'Qiita', 'description': 'Buy milk'}>]
