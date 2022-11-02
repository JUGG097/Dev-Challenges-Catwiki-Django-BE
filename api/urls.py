from django.urls import path
from .views import (
    health_check,
    get_top_ten,
    get_cat_details,
    get_cat_photos,
    get_cat_breeds,
)


urlpatterns = [
    path("check", health_check),
    path("topTen", get_top_ten),
    path("details/<str:cat_id>", get_cat_details),
    path("photos/<str:cat_id>", get_cat_photos),
    path("breedlist", get_cat_breeds),
]
