from pydantic import BaseModel
from datetime import date
from typing import List


class User(BaseModel):
    name: str
    date_of_birth: str
    email: str
    gender: str
    vector_embeddings: List[List[str]]
    phone_number: str
    photo_ids: List[float]
