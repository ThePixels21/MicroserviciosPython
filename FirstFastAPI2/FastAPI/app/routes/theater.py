from fastapi import APIRouter, Body
from ..schemas.theater_schema import Theater

theater_route = APIRouter()

@theater_route.get("/")
def get_all_theaters():
    try:
        return "All theaters"
    except Exception as e:
        print(e)
        return {"error": str(e)}


@theater_route.get("/{theaterId}")
def get_theater(theaterId: int):
    try:
        return theaterId
    except Exception as e:
        print(e)
        return {"error": str(e)}

@theater_route.post("/")
def create_theater(theater: Theater = Body(...)):
    try:
        return theater
    except Exception as e:
        print(e)
        return {"error": str(e)}

@theater_route.put("/")
def update_theater(theater: Theater = Body(...)):
    try:
        return theater
    except Exception as e:
        print(e)
        return {"error": str(e)}

@theater_route.delete("/{theaterId}")
def delete_theater(theaterId: int):
    try:
        return theaterId
    except Exception as e:
        print(e)
        return {"error": str(e)}