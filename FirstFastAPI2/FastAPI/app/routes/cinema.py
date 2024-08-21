from fastapi import APIRouter, Body
from ..schemas.cinema_schema import Cinema

cinema_route = APIRouter()


@cinema_route.get("/")
def get_all_cinemas():
    try:
        return "All cinemas"
    except Exception as e:
        print(e)
        return {"error": str(e)}


@cinema_route.get("/{cinemaId}")
def get_cinema(cinemaId: int):
    try:
        return cinemaId
    except Exception as e:
        print(e)
        return {"error": str(e)}

@cinema_route.post("/")
def create_cinema(cinema: Cinema = Body(...)):
    try:
        return cinema
    except Exception as e:
        print(e)
        return {"error": str(e)}

@cinema_route.put("/")
def update_cinema(cinema: Cinema = Body(...)):
    try:
        return cinema
    except Exception as e:
        print(e)
        return {"error": str(e)}

@cinema_route.delete("/{cinemaId}")
def delete_cinema(cinemaId: int):
    try:
        return cinemaId
    except Exception as e:
        print(e)
        return {"error": str(e)}