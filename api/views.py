from .helpers import extract_cat_details, extract_breed_details
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .third_party import catwiki


@api_view(["GET"])
def health_check(request):
    return Response({"success": True}, 200)


@api_view(["GET"])
def get_top_ten(request):
    catapi_first_ten = catwiki.get_breeds("topTen")
    if catapi_first_ten.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    json_payload = catapi_first_ten.json()

    return Response(
        {"success": True, "data": [extract_cat_details(i) for i in json_payload]}, 200
    )


@api_view(["GET"])
def get_cat_details(request, cat_id):
    catapi_breed_details = catwiki.get_breeds("details", cat_id)
    if catapi_breed_details.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    details_json_payload = catapi_breed_details.json()

    catapi_breed_image = catwiki.get_cat_images(cat_id, "1")
    if catapi_breed_image.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    images_json_payload = catapi_breed_image.json()
    details_json_payload["image"] = images_json_payload[0]

    return Response(
        {"success": True, "data": extract_cat_details(details_json_payload)}, 200
    )


@api_view(["GET"])
def get_cat_photos(request, cat_id):
    catapi_breed_images = catwiki.get_cat_images(cat_id, "8")
    if catapi_breed_images.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    images_json_payload = catapi_breed_images.json()

    return Response({"success": True, "data": images_json_payload}, 200)


@api_view(["GET"])
def get_cat_breeds(request):
    catapi_breeds = catwiki.get_breeds("breed_list")
    if catapi_breeds.status_code != 200:
        return Response({"success": False, "message": "3rd party API unreachable"}, 503)

    json_payload = catapi_breeds.json()

    return Response(
        {"success": True, "data": [extract_breed_details(i) for i in json_payload]}, 200
    )
