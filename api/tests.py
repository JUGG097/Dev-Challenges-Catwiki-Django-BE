from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import responses
from .helpers import (
    extract_breed_details,
    mock_breed_list_data,
    extract_cat_details,
    mock_cat_detail,
    mock_image_search,
)


class CatwikiTests(APITestCase):
    @responses.activate
    def test_get_top_ten(self):
        """
        Tests get_top_ten
        """
        responses.add(
            responses.GET,
            "https://api.thecatapi.com/v1/breeds?limit=10&page=0",
            json=mock_breed_list_data(),
            status=200,
        )

        url = reverse("topTen")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "success": True,
                "data": [extract_cat_details(i) for i in mock_breed_list_data()],
            },
        )

    @responses.activate
    def test_get_top_ten_503(self):
        """
        Tests get_top_ten failure
        """
        responses.add(
            responses.GET,
            "https://api.thecatapi.com/v1/breeds?limit=10&page=0",
            json=mock_breed_list_data(),
            status=400,
        )

        url = reverse("topTen")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)

    @responses.activate
    def test_get_details(self):
        """
        Tests get_cat_details
        """
        cat_id = "beng"
        responses.add(
            responses.GET,
            "https://api.thecatapi.com/v1/breeds/" + cat_id,
            json=mock_cat_detail(),
            status=200,
        )
        responses.add(
            responses.GET,
            "https://api.thecatapi.com/v1/images/search?page=0&limit=1"
            + "&breed_ids="
            + cat_id
            + "&include_breeds=false",
            json=mock_image_search(),
            status=200,
        )

        url = reverse("cat_details", args=[cat_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        modified_response = mock_cat_detail()
        modified_response["image"] = mock_image_search()[0]

        self.assertEqual(
            response.json(),
            {
                "success": True,
                "data": extract_cat_details(modified_response),
            },
        )

    @responses.activate
    def test_get_details_503(self):
        """
        Tests get_cat_details failure
        """
        cat_id = "beng"
        responses.add(
            responses.GET,
            "https://api.thecatapi.com/v1/breeds/" + cat_id,
            json=mock_cat_detail(),
            status=400,
        )

        url = reverse("cat_details", args=[cat_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)

    @responses.activate
    def test_get_photos(self):
        """
        Tests get_photos
        """
        cat_id = "beng"
        responses.add(
            responses.GET,
            "https://api.thecatapi.com/v1/images/search?page=0&limit=8"
            + "&breed_ids="
            + cat_id
            + "&include_breeds=false",
            json=mock_image_search(),
            status=200,
        )

        url = reverse("cat_photos", args=[cat_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "success": True,
                "data": mock_image_search(),
            },
        )

    @responses.activate
    def test_get_photos_503(self):
        """
        Tests get_photos failure
        """
        cat_id = "beng"
        responses.add(
            responses.GET,
            "https://api.thecatapi.com/v1/images/search?page=0&limit=8"
            + "&breed_ids="
            + cat_id
            + "&include_breeds=false",
            json=mock_image_search(),
            status=400,
        )

        url = reverse("cat_photos", args=[cat_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)

    @responses.activate
    def test_get_breedlist(self):
        """
        Tests get_breedlist
        """
        responses.add(
            responses.GET,
            "https://api.thecatapi.com/v1/breeds",
            json=mock_breed_list_data(),
            status=200,
        )

        url = reverse("cat_breeds")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "success": True,
                "data": [extract_breed_details(i) for i in mock_breed_list_data()],
            },
        )

    @responses.activate
    def test_get_breedlist_503(self):
        """
        Tests get_breedlist failure
        """
        responses.add(
            responses.GET,
            "https://api.thecatapi.com/v1/breeds",
            json=mock_breed_list_data(),
            status=400,
        )

        url = reverse("cat_breeds")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
