from api.v1.endpoints.genre import router as genre_router
from api.v1.endpoints.movie import router as movie_router
from api.v1.endpoints.studio import router as studio_router
from api.v1.endpoints.country import router as country_router
from api.v1.endpoints.season import router as season_router
from api.v1.endpoints.series import router as series_router


api_routers = [genre_router, movie_router, studio_router, country_router, season_router, series_router]