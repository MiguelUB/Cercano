"""
This program will extract from Google Places API through the API the data to fill our database
The main two functions will be to extract general information through coordinates and get the places ID from a search and
obtain details of the place such as photos, schedule, ratings, etc
"""

import math
from geopy.distance import distance

# Barcelona coordinates 41.38879, 2.15899 and the radius should 10Km

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

type_bussines = ['bakery','bar', 'beauty_salon','bicycle_store','cafe','car_repair','clothing_store','convenience_store',
'dentist', 'electronics_store','florist','hair_care','hardware_store','home_goods_store','locksmith',
'painter', 'pet_store','plumber','restaurant','shoe_store']

def hexagonal_pack(center_lat, center_lon, radius):
    """Función que devuelve las 6 coordenadas geográficas alrededor del centro"""

    # Calcular la distancia entre el centro y cada uno de los puntos circundantes
    distance = radius * math.sqrt(3)

    # Crear un set para almacenar las coordenadas
    coordinates = {(center_lat, center_lon)}

    # Calcular las coordenadas para cada punto circundante
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        lat = round(center_lat + (distance / 111.32) * math.cos(angle_rad), 5)
        lon = round(center_lon + (distance / (111.32 * math.cos(math.radians(center_lat)))) * math.sin(angle_rad), 5)
        coordinates.add((lat, lon))

    return coordinates


def distance_less_than(lat1, lon1, lat2, lon2, distance_less=100):
    # Creamos los puntos de latitud y longitud para los dos lugares
    p1 = (lat1, lon1)
    p2 = (lat2, lon2)

    # Calculamos la distancia entre los dos puntos utilizando la función "distance" de geopy
    dist = distance(p1, p2).meters

    # Devolvemos True si la distancia es menor que distance_less metros, y False en caso contrario
    return dist < distance_less

def get_coordinates( latitude, longitude, radius=1, layers=1):
    """
    This function will find all the locations in a radius given and a latitude and longitude as the center and create
    and save it all in a JSON
    :param float latitude :Latitude coordinate
    :param float longitude :Longitude coordinate
    :param int radius : Radius in km
    :param str json_name: Name for the json file
    :param int layers: Number of circles to have
    """
    coordinates = {(latitude, longitude)}
    current_coordinate = [(latitude, longitude)]
    radius_in_meters = radius * 1000

    # Conseguir todas las coordenadas dentro del radio usando empaquetamiento de circulos para maximizar los resultados
    for i in range(layers):
        for c_coord in current_coordinate:
            hexagonal_coordinates = hexagonal_pack(c_coord[0], c_coord[1], radius)
            for coord in current_coordinate:
                for hex_coord in hexagonal_coordinates:
                    if not distance_less_than(hex_coord[0], hex_coord[1], coord[0], coord[1], radius_in_meters - 100):
                        coordinates.add((hex_coord[0], hex_coord[1]))

        current_coordinate = coordinates.copy()
    return coordinates

gg = get_coordinates( 41.38879, 2.15899,1,1)
for i in gg:
    print(i[0],',',i[1])





