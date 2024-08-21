from datetime import datetime
from typing import List

from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    name: str
    description: str
    actors: List[str]
    releaseDate: datetime