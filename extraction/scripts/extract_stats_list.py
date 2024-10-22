import os
import requests
import pandas as pd


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url_api = "https://drop-api.ea.com/rating/ea-sports-fc?locale=en&limit=100"
    

response = requests.get(url_api,headers=headers)
response.raise_for_status()

data = response.json()
players = data["items"][:2]

stats_features = set()
for player in players:
    # Flatten the stats dictionary to include it in player_dict
    for stat_name, stat_info in player["stats"].items():
        stats_features.add(stat_name)


print("Extraction of stats finished.")

            
stats = pd.DataFrame(list(stats_features), columns=['stats'])
stats.to_csv(os.path.join('data','raw', f"stats_list.csv"), encoding='utf-8')