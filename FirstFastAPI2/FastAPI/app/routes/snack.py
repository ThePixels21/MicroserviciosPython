from fastapi import APIRouter, Body
from ..schemas.snack_schema import Snack

snack_route = APIRouter()

@snack_route.get("/")
def get_all_snacks():
    try:
        return "All snacks"
    except Exception as e:
        print(e)
        return {"error": str(e)}


@snack_route.get("/{snackId}")
def get_snack(snackId: int):
    try:
        return snackId
    except Exception as e:
        print(e)
        return {"error": str(e)}

@snack_route.post("/")
def create_snack(snack: Snack = Body(...)):
    try:
        return snack
    except Exception as e:
        print(e)
        return {"error": str(e)}

@snack_route.put("/")
def update_snack(snack: Snack = Body(...)):
    try:
        return snack
    except Exception as e:
        print(e)
        return {"error": str(e)}

@snack_route.delete("/{snackId}")
def delete_snack(snackId: int):
    try:
        return snackId
    except Exception as e:
        print(e)
        return {"error": str(e)}