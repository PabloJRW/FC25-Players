import requests
import datetime as dt


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url_api = "https://drop-api.ea.com/rating/ea-sports-fc?locale=en&limit=100"
response = requests.get(url_api,headers=headers)

data = response.json()

players = data["items"][:2]

for player in players:
    print(player["firstName"])
    print(player["lastName"])
    print(player["commonName"])
    print(player["gender"]["id"])
    print(player["height"])
    print(player["weight"])
    print(player["nationality"]["label"])
    print(player["birthdate"])
    print(player["position"]["positionType"]["id"])
    print(player["position"]["shortLabel"])
    alternatePositions = [position["shortLabel"] for position in player["alternatePositions"]]
    print(alternatePositions)
    print(player["preferredFoot"])
    print(player["leagueName"])
    print(player["team"]["label"])
    for ability_info in player["playerAbilities"]:
        ability_name = ability_info["label"]
        print(ability_name)

    for stat_name, stat_info in player["stats"].items():
        value = stat_info["value"]
        print(f"{stat_name}: {value}")
    
    print(player["weakFootAbility"])
    print(player["skillMoves"])
    
    print(player["overallRating"])
    
    print()