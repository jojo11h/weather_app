import json


def readfile(file):
    with open(file) as f:
        data = json.load(f)
    return data


def make_message(data):
    temp_celcius = data['main']['temp']-273.15
    weather = data['weather'][0]['description'].split()[-1]
    wind = data['wind']['speed'] * 1.609344

    ville = f"Ville : {data['name']}"
    temp = f"Temperature : {temp_celcius:.2f} °C"
    ciel = f"Ciel : {weather}"
    vent = f"Vitesse du vent : {wind:.2f} km/h"

    message = f"{ville},{temp},{ciel},{vent}"

    return message


if __name__ == '__main__':
    data = readfile('file.json')
    message = make_message(data)
    print(message)
