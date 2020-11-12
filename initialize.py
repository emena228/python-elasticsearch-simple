from datetime import datetime
from random import randint

from elasticsearch import Elasticsearch

indices = ['project_1', 'project_2', 'project_3']


def generate_random_document():
    return {
        'doc_id': randint(1000, 9999),
        'last_updated': datetime.now()
    }


def initialize():
    # Assume Elasticsearch is installed to the localhost with default port.
    es = Elasticsearch()

    for index in indices:
        es.indices.create(index=index, ignore=[404, 400])
        doc_count = randint(3, 5)

        for i in range(doc_count):
            es.index(index=index, id=i+1, body=generate_random_document())


initialize()
