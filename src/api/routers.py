from api.v1.endpoints.genre import router as genre_router
from api.v1.endpoints.movie import router as movie_router
from api.v1.endpoints.studio import router as studio_router
from api.v1.endpoints.country import router as country_router


api_routers = [genre_router, movie_router, studio_router, country_router]