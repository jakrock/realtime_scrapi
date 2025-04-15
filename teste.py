


import requests
# URL de l'API

url='https://wepari.com/service-api/LiveFeed/Get1x2_VZip?sports=1&count=4000&lng=fr&mode=4&country=182&getEmpty=true&virtualSports=true'

# url api pour les information pour les sports en general

# version lourd https://wepari.com/service-api/LineFeed/GetSportsShortZip?lng=fr&country=182&partner=386&virtualSports=true&gr=1309&groupChamps=true&tsTo=1746057600
#version legere https://wepari.com/service-api/LineFeed/GetSportsShortZip?lng=fr&country=182&virtualSports=true&groupChamps=true

# https://wepari.com/service-api/LineFeed/Get1x2_VZip?count=40&lng=fr&mode=4&country=182&partner=386&virtualSports=true&tsTo=1746057600
# https://wepari.com/service-api/LineFeed/Get1x2_VZip?sports=1&champs=214147&count=40&lng=fr&mode=4&country=182&partner=386&getEmpty=true&virtualSports=true&tsTo=1746057600

# url api pour les information pour les sports en general
# # https://wepari.com/service-api/LineFeed/GetSportsShortZip?sports=1&champs=214147&lng=fr&country=182&partner=386&virtualSports=true&gr=1309&groupChamps=true&tsTo=1746057600

#api pour les information pour les sports en detail par exemple le foot
# https://wepari.com/service-api/LineFeed/GetSportsShortZip?sports=1&lng=fr&country=182&groupChamps=true 

# Envoyer une requête GET
try:
    response = requests.get(url)
    response.raise_for_status()  # Vérifie si la requête a réussi (code 200)
    data = response.json()  # Convertir la réponse en JSON
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête : {e}")
print(len(data['Value']))  # Afficher la longueur de la liste 'Value' dans le JSON
