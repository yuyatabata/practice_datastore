from google.cloud import datastore

client = datastore.Client()

query = client.query(kind="media_table_structure")
for entity in list(query.fetch()):
    print(entity.key.parent)

# entities = [entity_to_dict(entity) for entity in query.fetch()]

# for entity in entities:
#     entity['parent'] = str(entity.pop("parent_key"))

print(entity.key.parent)