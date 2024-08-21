from pydantic import BaseModel

from .cinema_schema import Cinema
from .movie_schema import Movie

class Theater(BaseModel):
    id: int
    theaterNumber: int
    peopleInside: str
    playing: Movie | None
    capacity: int
    cinema: Cinema
