import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("customer_memory")


def save_memory(user_id, text, convo_id):
    collection.add(documents=[text], metadatas=[{"user_id": user_id}], ids=[convo_id])


def load_memory(query):
    return collection.query(query_texts=[query], n_results=3)
