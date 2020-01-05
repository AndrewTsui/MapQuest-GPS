import project3_api

#each ouput has to be a class
class Steps:
    '''
    Prints out each maneuver that needs to be made from location to location.
    '''
    def output(self, data: dict) -> str:
        print()
        print('DIRECTIONS')
        steps = []
        for legs in range(len(data['route']['legs'])):
            for moves in range(len(data['route']['legs'][legs]['maneuvers'])):
                steps.append(data['route']['legs'][legs]['maneuvers'][moves]['narrative'])
        for index in steps:
            print(index)
            
class Distance:
    '''
    Prints out the total distance for the entire trip.
    '''
    def output(self, data: dict) -> str:
        distance = data['route']['distance']
        distance = str(round(distance))
        print()
        print('TOTAL DISTANCE: ' + distance + ' miles')

class Time:
    '''
    Prints out the total time for the entire trip.
    '''
    def output(self, data: dict) -> str:
        time = data['route']['time']/60
        time = str(round(time))
        print()
        print('TOTAL TIME: ' + time + ' minutes')

class LatitudeLongitude:
    '''
    Prints out the latitude and longitude of each location in
    the order they were inputted.
    '''
    def __init__(self, num_locations: int):
        self._numlocations = num_locations
        
    def output(self, data: dict) -> str:
        print()
        print('LATLONGS')
        latlong = []
        for index in range(self._numlocations):
            long = data['route']['locations'][index]['displayLatLng']['lng']
            lat = data['route']['locations'][index]['displayLatLng']['lat']
            if lat < 0:
                pos = lat * -1
                latitude = '%.2f' % pos + 'S'
            else:
                latitude = '%.2f' % lat + 'N'
            if long < 0:
                pos = long*-1
                longitude = '%.2f' % pos + 'W'
            else:
                longitude = '%.2f' % long + 'E'
            latlong.append(latitude + ' ' + longitude)
        for index in latlong:
            print(index)

class Elevation:
    '''
    Prints out the elevation in feet of each location in the
    order they were inputted.
    '''
    def __init__(self, num_locations: int):
        self._numlocations = num_locations
        
    def output(self, data: dict) -> str:
        #gets the latitudes and longitudes of each location
        elevation_latlong = []
        for i in range(self._numlocations):
            long = data['route']['locations'][i]['displayLatLng']['lng']
            lat = data['route']['locations'][i]['displayLatLng']['lat']
            elevation_latlong.append(str(lat))
            elevation_latlong.append(str(long))

        distance = data['route']['distance']
        distance = round(distance)
        
        print()
        print('ELEVATIONS')
        if distance > 250:
            counter = 0
            #divide by two because each location has a latitude and longitude
            x = int(len(elevation_latlong)/2)
            elevations = []
            for i in range(x):
                elevation = project3_api.build_elevation_url(elevation_latlong[counter:counter+2])
                info = project3_api.get_result(elevation)
                for i in range(len(info['elevationProfile'])):
                    elevations.append(round(info['elevationProfile'][i]['height']))
                counter += 2
            else:
                for i in range(x):
                    elevation = project3_api.build_elevation_url(elevation_latlong[counter:counter+2])
                    info = project3_api.get_result(elevation)
                    for i in range(len(info['elevationProfile'])):
                        elevations.append(round(info['elevationProfile'][i]['height']))
            for i in elevations:
                print(i)

class NoRoute:
    '''
    MapQuest cannot find a route.
    '''
    def output(self, data: dict) -> int:
        if data['info']['statuscode'] == 402:
            return 0
        else:
            return 1

class Error:
    '''
    There is an error other than a route not being found with MapQuest.
    '''
    def output(self) -> str:
        print()
        print('MAPQUEST ERROR')

class Copyright:
    '''
    Prints out the copyright message.
    '''
    def output(self) -> str:
        print()
        print('Directions Courtesy of MapQuest: Map Data Copyright OpenStreetMap Contributors')

def run_outputs(outputs: ['Outputs'], data: dict) -> str:
    '''
    Asks each class for its output, then prints out the results.
    '''
    if NoRoute().output(data) == 0:
        print()
        print('NO ROUTE FOUND')
    else:
        output_list = []
        for output_type in outputs:
            output_list.append(output_type.output(data))
        Copyright().output()

