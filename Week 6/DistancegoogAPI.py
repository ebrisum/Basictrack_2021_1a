import json
import requests

#API key from Google maps IPA:
key = 'AIzaSyA0tkG51rUfuiLc8q1ohAdYYq8zpK4qvv0'

#Ask for user input: mode of transportation

mode = input("What is your type of transport: (walking, bicycling, driving, transit) ")
if mode =='transit':
    transit_mode= input("What type of public transport do you use?: (bus, tram, subway, train, rail) ")
    if transit_mode == "rail":
        transit_mode = train|tram|subway
else:
    transit_mode= None



    params = {
    'key': key,
    'origins': input("Where are you now: "),
    'destinations': input("What is your destination: "),
    'mode': mode,
    'deperature_time': now
    }


#Creating functions to be able to provide directions !UNDER CONSTRUCTION!
def directionsAB(origins, destination, mode, transit_mode):
    key = 'AIzaSyAnCobNK7GDHm3PiJusGNbeZh2y_AGsH00'
    params = {
    'key': key,
    'origin': origins,
    'destination': destination,
    'mode': mode
    }

    if mode == "transit":
        if transit_mode == "train":
            url = ('https://maps.googleapis.com/maps/api/directions/json?'
                   + '&mode={}'
                   + '&transit_mode={}'
                   ).format(mode, transit_mode)
            response = requests.get(url, params)
            result = json.loads(response.text)
            print(response.text)
            endpoint = result['routes'][0]['legs'][0]['arrival_time']['text']
            startpoint = result['routes'][0]['legs'][0]['departure_time']['text']
            print("The train leaves at: "+ startpoint +" in " +origins + " and arrives at: " + endpoint + " in "+ destination)

    elif mode == 'walking':
        duration = int(result['routes'][0]['legs']['steps'][1]['duration']['value']/60)
        if duration>180:
            print('The best option is to consider taking public transport or car!')
            car_transit= input('Is that an option? (yes/no)')
            if car_transit == 'yes':
                distance_Duration(origins, destination, driving, None)
            else:
                print(None)

    else:
        print("No")
        print(startpoint)



#directionsAB('Leeuwarden', 'Groningen', 'transit', 'train')
distance_Duration(key, mode, transit_mode)
