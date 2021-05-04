import os
import sys

from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#  print(es.ping())

#  es.indices.create(index='computer-games', ignore=400)

#  res = es.indices.get_alias("*")

#  for Name in res:
#      print(Name)

account_with_id_1 = es.get(index="bank", id=1)
print(account_with_id_1['_source'])

all_accounts = es.search(index="bank", body={"query": {"match_all": {}}}, size=1001) #  Default size is 10

print(f"Got {all_accounts['hits']['total']['value']} Hits:")
for hit in all_accounts['hits']['hits']:
    print(f"id: {hit['_id']}, name: {hit['_source']['firstname']} {hit['_source']['lastname']}")

print('---------------------------------------------')

all_accounts_from_IL = es.search(index="bank", body={"query": {"match": {'state': 'IL'}}}, size=100)
for hit in all_accounts_from_IL['hits']['hits']:
    print(f"id: {hit['_id']}, name: {hit['_source']['firstname']} {hit['_source']['lastname']}")

print('---------------------------------------------')
account_to_add = {
    "account_number": 1002,
    "balance": 20,
    "firstname": "Amy",
    "lastname": "Fernandez",
    "age": 21,
    "gender": "F",
    "address": "999 Johnson  Street",
    "employer": "Geofarm",
    "email": "amyfernandez@corepan.com",
    "city": "Worcester",
    "state": "KS"
}

#  added_account = es.index(index='bank', id=1002, body=account_to_add)
#  print(added_account)

account_with_id_1002 = es.get(index="bank", id=1002)
print(account_with_id_1002['_source'])

#  delete_res = es.delete(index='bank', id=1002)
#  print(delete_res['result'])

