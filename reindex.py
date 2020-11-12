from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch.helpers import reindex


def reindex_and_update(wildcard='*'):
    # Assume Elasticsearch is installed to localhost with default port.
    es = Elasticsearch()
    target_index = 'merged'
    es.indices.delete(index=target_index)

    reindex(
        client=es,
        source_index=wildcard,
        target_index=target_index
    )

    es.update_by_query(
        index=target_index,
        body={
            'query': {
                'exists': {
                    'field': 'last_updated'
                }
            },
            'script': {
                'source': 'ctx._source.last_updated = \'{}\''.format(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))
            }
        }
    )


reindex_and_update('project_*')
