import mapquest_api
import mapquest_outputs

def main():
    try:
        location_number = number_of_locations()
        location_list = locations(location_number)
        completed_url = mapquest_api.build_search_url(location_list)
        converted_json_text = mapquest_api.get_result(completed_url)
        number_outputs = number_of_outputs()
        outputs_list = return_outputs_list(number_outputs) 
        latLng_list = return_lat_long(converted_json_text)
        elevation_URL = mapquest_api.build_elevation_url(latLng_list)
        converted_json_elevation = mapquest_api.get_result(elevation_URL)
        print_output(converted_json_text, outputs_list, converted_json_elevation)
        print('\n' + 'Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    except KeyError:
        print()
        print('NO ROUTE FOUND')
    except:
        print()
        print('MAPQUEST ERROR')

def number_of_locations():
    '''
    The Number of Locations the user enters
    '''
    number_locations = int(input('How many locations are you entering? '))
    if number_locations >= 2:
        return number_locations

def locations(location_number):
    '''
    The Location Names the user enters according to their number
    '''
    location_list = []
    for numbers in range(location_number):
        location_names = input('Enter your locations, one at a time: ')
        location_list.append(location_names)
    return location_list

def number_of_outputs():
    '''
    The Number of Outputs the user wants (5 possible)
    '''
    print('How many of these would you like? Enter a number: STEPS, TOTALTIME, TOTALDISTANCE, LATLONG, ELEVATION ')
    number_outputs = input('STEPS, TOTALTIME, TOTALDISTANCE, LATLONG, ELEVATION ')
    print()
    return int(number_outputs)

def return_outputs_list(number_of_outputs):
    '''
    Appends the User's Outputs to a list
    '''
    outputs_list = []
    for numbers in range(number_of_outputs):
       output_choices = input('Enter the choices you made')
       outputs_list.append(output_choices)
    return outputs_list

def return_lat_long(converted_json_text):
    '''
    Returns a list of latitudes and longitudes for the elevation to be acessed
    '''
    lat_lng_list = []
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
        lat_lng_list.append(lat)
        lat_lng_list.append(lng)
    return lat_lng_list

def print_output(converted_json_text, outputs_list, converted_json_elevation):
    '''
    Prints the Outputs
    '''
    for outputs in outputs_list:
        if outputs == 'LATLONG':
            mapquest_outputs.lat_long().get_method(converted_json_text)
            print()
        elif outputs == 'STEPS':
            mapquest_outputs.steps().get_method(converted_json_text)
            print()
        elif outputs == 'TOTALTIME':
            mapquest_outputs.total_time().get_method(converted_json_text)
            print()
        elif outputs == 'TOTALDISTANCE':
            mapquest_outputs.total_distance().get_method(converted_json_text)
            print()
        elif outputs == 'ELEVATION':
            mapquest_outputs.elevation().get_method(converted_json_elevation)
            print()

if __name__ == '__main__':
    main()
