from pydantic import BaseModel

from .cinema_schema import Cinema


class Snack(BaseModel):
    id: int
    name: str
    description: str
    type: str
    price: float
    cinema: Cinema