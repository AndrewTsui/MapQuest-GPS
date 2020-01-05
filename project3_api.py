import urllib.request
import urllib.parse
import json

BASE_MAPQUEST_DESTINATION_URL = 'http://open.mapquestapi.com/directions/v2/route'
BASE_MAPQUEST_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile'
MAPQUEST_API_KEY = 'hIZ98AIBoOx3ZiEH2562DAwJYyuiMCXA'

def build_destination_url(places: [str]) -> str:
    '''
    Creates the URL for the route. If there are multiple destinations,
    adds the extra destinations to the end.
    '''
    parameters = [
        ('key', MAPQUEST_API_KEY), ('from', places[0])
    ]
    del places[0]
    for index in range(len(places)):
        parameters.append(('to', places[index]))
    return BASE_MAPQUEST_DESTINATION_URL+'?'+urllib.parse.urlencode(parameters)

def build_elevation_url(lat_long: [str]) -> str:
    '''
    Creates the URL for the elevation. Attaches all the latitudes
    and longitudes of the destinations.
    '''
    parameters = [
        ('key', MAPQUEST_API_KEY), ('shapeFormat', 'raw')
    ]
    url = BASE_MAPQUEST_ELEVATION_URL+'?'+urllib.parse.urlencode(parameters)+'&latLngCollection='
    counter = 0
    for latlong in lat_long:
        if counter != len(lat_long)-1:
            url = url + latlong + ','
            counter += 1
        else:
            url = url + latlong

    #turns the units to feet
    url = url + '&unit=f'
    return url

def get_result(url: str) -> 'json text':
    '''
    Returns the result from reading the URL
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.load(response)
    finally:
        if response!= None:
            response.close()
