import requests
from api.helpers import auth_header


def get_breeds(calling_key: str, cat_id=None):
    if calling_key == "topTen":
        return requests.get(
            "https://api.thecatapi.com/v1/breeds?limit=10&page=0", headers=auth_header()
        )
    elif calling_key == "details":
        return requests.get(
            "https://api.thecatapi.com/v1/breeds/" + cat_id, headers=auth_header()
        )
    else:
        return requests.get(
            "https://api.thecatapi.com/v1/breeds", headers=auth_header()
        )


def get_cat_images(cat_id: str, num_of_photos: str):
    return requests.get(
        "https://api.thecatapi.com/v1/images/search?page=0&limit="
        + num_of_photos
        + "&breed_ids="
        + cat_id
        + "&include_breeds=false",
        headers=auth_header(),
    )
