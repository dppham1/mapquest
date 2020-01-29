import json
import urllib.parse
import urllib.request

MAPQUEST_KEY = 'LjV8AdyWzZlYbskuWpM3Fr8t5BHzuB7B'

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?'

BASE_MAPQUEST_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'

def build_search_url(location_list):
    '''The function builds a SEARCH URL that will be used to extract data from'''
    query_parameters = [
        ('key', MAPQUEST_KEY), ('from', location_list[0])
        ]
    for numbers in range(len(location_list)-1):
        query_parameters.append(('to', location_list[numbers+1]))
        URL_parameters = urllib.parse.urlencode(query_parameters)
        URL_entire = BASE_MAPQUEST_URL + URL_parameters
    return URL_entire

def build_elevation_url(latlng_list):
    '''The Function builds a ELEVATION URL that will be used to extract elevations
    from'''
    empty_string = ''
    for indexes in range(len(latlng_list)):
        empty_string += str(latlng_list[indexes]) + ','
    query_parameters = [
        ('key', MAPQUEST_KEY), ('latLngCollection', empty_string),
        ('unit', 'f')
        ]
    URL_parameters = urllib.parse.urlencode(query_parameters)
    URL_entire = BASE_MAPQUEST_ELEVATION_URL + URL_parameters
    return URL_entire

def get_result(url: str) -> 'json':
    '''
    Takes a URL string and returns a Python object representing the
    parsed JSON response.
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()
