from model import User
from database import (
    create_collection,
    get_collection,
    add_documents,
    query_documents,
    get_documents,
    update_documents,
    delete_documents,
)


# Function to create a collection for users
async def create_user_collection(name="Users"):
    return create_collection(name)


# Function to get the user collection
async def get_user_collection(name="Users"):
    return get_collection(name)


# Function to add a user to the collection
async def add_user_to_collection(user_data: User):
    collection = await get_user_collection()
    return add_documents(collection, documents=[user_data.model_dump()])


# Function to find similar users in the collection
async def similarity_search(
    query_embeddings,
    n_results=10,
    where=None,
    where_document=None,
    include=None,
):
    collection = await get_user_collection()
    return collection.query_documents(
        query_embeddings=query_embeddings,
        n_results=n_results,
        where=where,
        where_document=where_document,
        include=include,
    )


# Function to get data from the collection
async def get_data(ids=None, where=None, include=None):
    collection = await get_user_collection()
    return get_documents(collection, ids=ids, where=where, include=include)


# Function to update user data in the collection
async def update_user_data(ids, user_data: User):
    collection = await get_user_collection()
    return update_documents(collection, ids=ids, documents=[user_data.model_dump()])


# Function to delete users from the collection
async def delete_users(ids=None, where=None):
    collection = await get_user_collection()
    return delete_documents(collection, ids=ids, where=where)
