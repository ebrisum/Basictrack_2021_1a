import json
import requests

#function that interacts with the google distance-matrix api
def distance_Duration(key, origin, destination, mode, transit_mode):
    """"
    input:
    key:            str (API key)
    origins:        str (input)
    destinations:   str (input)
    mode:           str
    transit_mode    str

    output:
    amount of kilometers:   float
    time of travel:         int

"""

    url =('https://maps.googleapis.com/maps/api/distancematrix/json?'
          + '&departure_time=now'
          + '&key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
          )

    response = requests.get(url, params)
    result = json.loads(response.text)
    #I like to see what the output of the json is, that's why I print it
    distance = result['rows'][0]['elements'][0]['distance']['value']
    distance = round(distance / 1000, 1)
    duration = result['rows'][0]['elements'][0]['duration']['value']
    duration = int(duration / 60)
    return duration, distance

#function for providing directions:
def directionsAB(origins, destination, mode, transit_mode):
    key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    params = {
    'key': key,
    'origin': origins,
    'destination': destination,
    'mode': mode
    }

    url = ('https://maps.googleapis.com/maps/api/directions/json?'
           + '&mode={}'
           + '&transit_mode={}'
           + '&language=nl'
           ).format(mode, transit_mode)
    response = requests.get(url, params)
    result = json.loads(response.text)
    instructions = result["routes"][0]['legs'][0]['steps']
    final_instructions=[]
    for i in instructions:
        final_instructions.append(i['html_instructions'])
    return final_instructions

#ask for user inputs for all arguments used in functions
origins = input("Where are you now?: ")
destination = input("What is your destination: ")
mode= input("What is your type of transport: (walking, bicycling, driving, transit) ")
if mode == 'transit':
    transit_mode = input("What type of public transport would you like to use?: (bus, tram, subway, train, all) ")
else:
    transit_mode = None

#API key from Google maps IPA (distance-matrix, directions):
key_dismatrix= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
key_dirmatrix= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#parameters used for requests from google API
params = {
    'origins': origins,
    'destinations': destination,
    'mode': mode,
    'transit_mode': transit_mode
    }

#storing duration and distance values in variable and outputting distance and duration
duration = distance_Duration(key_dismatrix, origins, destination, mode, transit_mode)[1]
distance = distance_Duration(key_dismatrix, origins, destination, mode, transit_mode)[0]
if duration<60:
    print("You will travel " + str(distance) + " kilometers, in a time of " + str(duration) + " minutes before you arrive at your destination")
else:
    print("You will travel " + str(distance) + " kilometers, in a time of " + str(int(duration/60)) + " hour(s) and " + str(int(
        duration % 60)) + " minutes before you arrive at your destination")

#option to call the direction api, when yes, directions will be provided
want_Direction = input("Would you like to receive directions? (yes/no)")
num = 1
if want_Direction == 'yes':
    for i in (directionsAB(origins, destination, mode, transit_mode)):
        print(str(num)+ ": " + i)
        num+= 1


