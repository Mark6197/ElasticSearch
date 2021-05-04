from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

es.indices.create(index='computer-games', ignore=400)

game_to_add = {
    "id": 1,
    "name": "Assassin's Creed",
    "company": "Ubisoft",
    "year": 2011,
}

es.index(index='computer-games', id=1, body=game_to_add)
game_with_id_1 = es.get(index="computer-games", id=1)
print(game_with_id_1['_source'])
