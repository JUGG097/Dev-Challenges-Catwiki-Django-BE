from .helpers import auth_header, extract_cat_details, extract_breed_details
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests


@api_view(["GET"])
def health_check(request):
    return Response({"success": True}, 200)


@api_view(["GET"])
def get_top_ten(request):
    catapi_first_ten = requests.get(
        "https://api.thecatapi.com/v1/breeds?limit=10&page=0", headers=auth_header()
    )
    if catapi_first_ten.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    json_payload = catapi_first_ten.json()

    return Response(
        {"success": True, "data": [extract_cat_details(i) for i in json_payload]}, 200
    )


@api_view(["GET"])
def get_cat_details(request, cat_id):
    catapi_breed_details = requests.get(
        "https://api.thecatapi.com/v1/breeds/" + cat_id, headers=auth_header()
    )
    if catapi_breed_details.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    details_json_payload = catapi_breed_details.json()

    catapi_breed_image = requests.get(
        "https://api.thecatapi.com/v1/images/search?page=0&limit=1&breed_ids="
        + cat_id
        + "&include_breeds=false",
        headers=auth_header(),
    )
    if catapi_breed_image.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    images_json_payload = catapi_breed_image.json()
    details_json_payload["image"] = images_json_payload[0]

    return Response(
        {"success": True, "data": extract_cat_details(details_json_payload)}, 200
    )


@api_view(["GET"])
def get_cat_photos(request, cat_id):
    catapi_breed_images = requests.get(
        "https://api.thecatapi.com/v1/images/search?page=0&limit=8&breed_ids="
        + cat_id
        + "&include_breeds=false",
        headers=auth_header(),
    )
    if catapi_breed_images.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    images_json_payload = catapi_breed_images.json()

    return Response({"success": True, "data": images_json_payload}, 200)


@api_view(["GET"])
def get_cat_breeds(request):
    catapi_breeds = requests.get(
        "https://api.thecatapi.com/v1/breeds", headers=auth_header()
    )
    if catapi_breeds.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    json_payload = catapi_breeds.json()

    return Response(
        {"success": True, "data": [extract_breed_details(i) for i in json_payload]}, 200
    )
