from fastapi import APIRouter, Body
from ..schemas.movie_schema import Movie

movie_route = APIRouter()

@movie_route.get("/")
def get_all_movies():
    try:
        return "All movies"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@movie_route.get("/{movieId}")
def get_movie(movieId: int):
    try:
        return movieId
    except Exception as e:
        print(e)
        return {"error": str(e)}

@movie_route.post("/")
def create_movie(movie: Movie = Body(...)):
    try:
        return movie
    except Exception as e:
        print(e)
        return {"error": str(e)}

@movie_route.put("/")
def update_movie(movie: Movie = Body(...)):
    try:
        return movie
    except Exception as e:
        print(e)
        return {"error": str(e)}

@movie_route.delete("/{movieId}")
def delete_movie(movieId: int):
    try:
        return movieId
    except Exception as e:
        print(e)
        return {"error": str(e)}