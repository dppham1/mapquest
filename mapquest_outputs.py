import json
import mapquest_api

class steps:
    def get_method(self, converted_json_text):
        '''
        Prints the directions from the json_text that has been converted
        into a python object
        '''
        print('DIRECTIONS')
        legs_list = converted_json_text['route']['legs']
        for dictionaries in legs_list:
            for keys in dictionaries['maneuvers']:
                print(keys['narrative'])
        
class total_distance:
    def get_method(self, converted_json_text):
        '''
        Prints the Total Distance of all routes added together
        '''
        for keys_route_and_info in converted_json_text:
            if keys_route_and_info == 'route':
                DISTANCE = converted_json_text[keys_route_and_info]['distance']
                print('TOTAL DISTANCE:', round(DISTANCE), 'miles')
            
class total_time:
    def get_method(self, converted_json_text):
        '''
        Prints the Total Time of all route times added together
        '''
        time_minutes = (converted_json_text['route']['time'])/60
        print('TOTAL TIME:', round(time_minutes), 'minutes')       

class lat_long:
    def get_method(self, converted_json_text):
        '''
        Prints the Latitudes and Longitudes extracted from the converted
        json text
        '''
        print('LATLONGS')
        empty_string_lng = ''
        empty_string_lat = ''
        for keys in converted_json_text['route']['locations']:
            lng = keys['latLng']['lng']
            lat = keys['latLng']['lat']
            rounded_lng = round(lng, 2)
            rounded_lat = round(lat, 2)
            if rounded_lng <= 0:
                empty_string_lng = 'W'
                rounded_lng = rounded_lng * -1
            else:
                empty_string_lng = 'E'
            if rounded_lat <= 0:
                empty_string_lat = 'S'
                rounded_lat = rounded_lat * -1
            else:
                empty_string_lat = 'N'
            print(str(rounded_lat) + empty_string_lat, str(rounded_lng) + empty_string_lng)

class elevation:
    def get_method(self, converted_json_text_elevation):
        '''
        Prints the Elevation of each location if below 250. If over 250,
        a MAPQUEST ERROR will be given, since Mapquest's API does not allow
        for elevations over 250
        '''
        print('ELEVATIONS')
        for indixes in range(len(converted_json_text_elevation)-1):
            print(round(converted_json_text_elevation['elevationProfile'][indixes]['height']))
