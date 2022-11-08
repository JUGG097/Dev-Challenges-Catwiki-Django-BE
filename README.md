# Catwiki Django Backend Project (The backend for the Catwiki Website deployed [here](https://catwiki-adeoluwa.netlify.app/))

This project was developed using `Python` v "^3.9", it runs `Django` v "^4.0.4", `Sentry-sdk` v "^1.5.11", and `Djangorestframework` v "^3.13.1" libraries.

Deployed on a `Digital Oceans` Droplet using `Github Actions` for CI/CD.

The Catwiki Website was deployed with `Netlify` link [here](https://catwiki-adeoluwa.netlify.app/).

Figma design was provided by [devChallenges.io](https://devchallenges.io/).

You can clone project and customise at your end.

### API Documentation

- 'http://127.0.0.1:8000/api/v1/topTen' Endpoint

METHOD: 'GET'

SUCCESS RESPONSE (200): {'success': true, 'data': '**********'}

ERROR RESPONSE (4**, 5**): {'success': false, 'message': '***********'}


- 'http://127.0.0.1:8000/api/v1/details/{cat_id}' Endpoint

METHOD: 'GET'

SUCCESS RESPONSE (200): {'success': true, 'data': '**********'}

ERROR RESPONSE (4**, 5**): {'success': false, 'message': '***********'}


- 'http://127.0.0.1:8000/api/v1/photos/{cat_id}' Endpoint

METHOD: 'GET'

SUCCESS RESPONSE (200): {'success': true, 'data': '**********'}

ERROR RESPONSE (4**, 5**): {'success': false, 'message': '***********'}

- 'http://127.0.0.1:8000/api/v1/breedlist' Endpoint

METHOD: 'GET'

SUCCESS RESPONSE (200): {'success': true, 'data': '**********'}

ERROR RESPONSE (4**, 5**): {'success': false, 'message': '***********'}