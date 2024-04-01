import chromadb

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="/pluralDB")


# Function to create a collection
def create_collection(name):
    return client.create_collection(name=name)


# Function to get a collection
def get_collection(name):
    return client.get_collection(name=name)


# Function to add documents to a collection
def add_documents(collection, documents, embeddings=None, metadatas=None, ids=None):
    return collection.add(
        documents=documents, embeddings=embeddings, metadatas=metadatas, ids=ids
    )


# Function to query documents in a collection
def query_documents(
    collection,
    query_embeddings,
    n_results=10,
    where=None,
    where_document=None,
    include=None,
):
    return collection.query(
        query_embeddings=query_embeddings,
        n_results=n_results,
        where=where,
        where_document=where_document,
        include=include,
    )


# Function to get documents from a collection
def get_documents(collection, ids=None, where=None, include=None):
    return collection.get(ids=ids, where=where, include=include)


# Function to update documents in a collection
def update_documents(collection, ids, documents=None, embeddings=None, metadatas=None):
    return collection.update(
        ids=ids, documents=documents, embeddings=embeddings, metadatas=metadatas
    )


# Function to upsert documents in a collection
def upsert_documents(collection, ids, documents=None, embeddings=None, metadatas=None):
    return collection.upsert(
        ids=ids, documents=documents, embeddings=embeddings, metadatas=metadatas
    )


# Function to delete documents from a collection
def delete_documents(collection, ids=None, where=None):
    return collection.delete(ids=ids, where=where)
