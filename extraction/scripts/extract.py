import os
import requests
import pandas as pd


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


num_of_pages = 176   # The web page has 175 pages of players
offset = 100   # Each page has 100 players
players_list = []
for i in range(num_of_pages):
    if i == 0:
        url_api = "https://drop-api.ea.com/rating/ea-sports-fc?locale=en&limit=100"
    else:
        url_api = f"https://drop-api.ea.com/rating/ea-sports-fc?locale=en&limit=100&offset={offset}"

    try:
        response = requests.get(url_api,headers=headers)
        response.raise_for_status()

        data = response.json()
        players = data["items"]

        for player in players:
            try:
                player_dict = {
                    "id_player": player["id"],
                    "first_name": player["firstName"],
                    "last_name": player["lastName"],
                    "common_name": player["commonName"],
                    "avatar_url": player["avatarUrl"],
                    "shield_url": player["shieldUrl"],
                    "gender_id": player["gender"]["id"],
                    "height": player["height"],
                    "weight": player["weight"],
                    "id_nationality": player["nationality"]["id"],
                    "nationality": player["nationality"]["label"],
                    "nationality_url": player["nationality"]["imageUrl"],
                    "birthdate": player["birthdate"],
                    "position": player["position"]["id"],
                    "position_type": player["position"]["positionType"]["name"],
                    "position_short_label": player["position"]["shortLabel"],
                    "position": player["position"]["label"],
                    "alternate_positions": ", ".join([position["shortLabel"] for position in player.get("alternatePositions", []) or []]),  # Convertir lista a cadena
                    "preferred_foot": player["preferredFoot"],
                    "league_name": player["leagueName"],
                    "team": player["team"]["id"],
                    "team": player["team"]["label"],
                    "team_image_url": player["team"]["imageUrl"],
                    "player_abilities": ", ".join([ability_info["label"] for ability_info in player.get("playerAbilities", []) or []]),  # Convertir lista a cadena
                    "weak_foot_ability": player["weakFootAbility"],
                    "skill_moves": player["skillMoves"],
                    "overall_rating": player["overallRating"]
                }
            
                # Flatten the stats dictionary to include it in player_dict
                for stat_name, stat_info in player["stats"].items():
                    player_dict[f"stat_{stat_name}"] = stat_info["value"]

                # Flatten the stats dictionary to include it in player_dict
                for stat_name, stat_info in player["stats"].items():
                    player_dict[f"diff_{stat_name}"] = stat_info["diff"]

                players_list.append(player_dict)

            except KeyError as e:
                print(f"Key error: {e} - skipping player.")
            except Exception as e:
                print(f"Unexpected error: {e} - Skipping player.")
    
    except requests.RequestException as e:
        print(f"Request failed at iteration {i}: {e}")
    except Exception as e:
        print(f"Unexpected error at iteration {i}: {e}")

    print(f"Players from page {i} has been extracted")
    offset += 100 # Increment the offset for the next page


# Convert the list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(players_list)

# Save the players data into a CSV file after each iteration
file_name = 'fc25players_10_21_2024_2'
df.to_csv(os.path.join('extraction','raw_data', f"{file_name}.csv"), encoding='utf-8', index=False)

print(f"Data saved to {file_name}.csv")
print(f"Last offset: {offset}")