import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

BESTTIME_API_URL = "https://besttime.app/api/v1/"
BESTTIME_API_KEY = ""

@csrf_exempt
@require_http_methods(['GET'])
def get_forecasts(venue_name, venue_address):
    url = BESTTIME_API_URL + "forecasts"

    params = {
        'api_key_private': BESTTIME_API_KEY,
        'venue_name': venue_name,
        'venue_address': venue_address
    }

    response = requests.post(url, params=params)
    data = response.json()
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(['GET'])
def get_venue_search(query):
    url = BESTTIME_API_URL + "venues/search"

    params = {
        'api_key_private': BESTTIME_API_KEY,
        'q': query,
        'num': 3,
        'fast': False,
        'format': 'raw'
    }

    response = requests.post(url, params=params)
    data = response.json()
    return JsonResponse(data, safe=False)