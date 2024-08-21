from typing import List

from pydantic import BaseModel
from .movie_schema import Movie

class Cinema(BaseModel):
    id: int
    name: str
    address: str
    movies: List[Movie]
    theatersCount: int