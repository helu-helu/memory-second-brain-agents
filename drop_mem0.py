import sys, os
sys.path.append('.')
from agent_core.config import MEM0_CONFIG
from qdrant_client import QdrantClient
from agent_core.config import config
client = QdrantClient(path=config["memory"]["qdrant"]["path"])
coll = MEM0_CONFIG['vector_store']['config']['collection_name']
if client.collection_exists(coll):
    client.delete_collection(coll)
    print(f'Deleted {coll}')
else:
    print(f'{coll} not found')
