from fastapi import FastAPI
from starlette.responses import RedirectResponse

#from .routes.cinema import cinema_route
#from .routes.movie import movie_route
#from .routes.snack import snack_route
#from .routes.theater import theater_route
#from .routes.user import user_route

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

# --------- USER ------------
#app.include_router(user_route, prefix = "/users", tags = ["Usuarios"])

# --------- MOVIE ------------
#app.include_router(movie_route, prefix = "/movies", tags = ["Películas"])

# --------- CINEMA ------------
#app.include_router(cinema_route, prefix = "/cinemas", tags = ["Cines"])

# --------- SNACK ------------
#app.include_router(snack_route, prefix = "/snacks", tags = ["Comidas"])

# --------- Theater ------------
#app.include_router(theater_route, prefix = "/theaters", tags = ["Teatros"])