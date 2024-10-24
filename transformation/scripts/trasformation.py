import os
import pandas as pd


def create_player_df(df):
    players_cols = ["id_player","first_name","last_name","common_name","avatar_url","shield_url","gender_id","height","weight","birthdate"]
    players_df = df[players_cols]
    players_df.set_index("id_player", inplace=True)
    return players_df


def create_gender_df(df):
    gender_cols = ["id_player", "gender_id"]
    gender_df = df[gender_cols].copy()
    gender_df.set_index("id_player", inplace=True)
    return gender_df  


def create_player_technical_df(df):
    player_technical_cols = ["id_player","preferred_foot",'weak_foot_ability', 'skill_moves', "overall_rating"]
    player_technical_df = df[player_technical_cols].copy()
    player_technical_df.set_index("id_player", inplace=True)
    return player_technical_df


def create_player_abilities_df(df):
    player_abilities_cols = ["id_player", "player_abilities"]
    player_abilities_df = df[player_abilities_cols].copy()
    player_abilities_df['player_abilities'] = player_abilities_df['player_abilities'].str.split(', ')
    player_abilities_df = player_abilities_df.explode('player_abilities').reset_index(drop=True)
    player_abilities_df.set_index("id_player", inplace=True)
    return player_abilities_df


def create_team_df(df):
    team_cols = ["id_player", "team", "league_name", "team_image_url"]
    team_df = df[team_cols].copy()
    team_df.set_index("id_player", inplace=True)
    return team_df


def create_nationality_df(df):
    nationality_cols = ["id_player", "id_nationality", "nationality", "nationality_url"]
    nationality_df = df[nationality_cols].copy()
    nationality_df.set_index("id_player", inplace=True)
    return nationality_df


def create_stats_df(df):
    stats_cols = df.filter(regex='^stat_').columns.tolist()
    stats_temp = df[["id_player"]+stats_cols].copy()
    stats_melted = pd.melt(stats_temp, id_vars=['id_player'], var_name='stats', value_name='stats_point')
    stats_melted['stats'] = stats_melted['stats'].str.replace('stat_', '')
    stats_melted = stats_melted.set_index('id_player')

    diff_stats_cols = df.filter(regex='^diff_').columns.tolist()
    diff_temp = df[["id_player"]+diff_stats_cols].copy()
    diff_melted = pd.melt(diff_temp, id_vars=['id_player'], var_name='diff_stats', value_name='diff_points')
    diff_melted['diff_stats'] = diff_melted['diff_stats'].str.replace('diff_', '')
    diff_stats_df = diff_melted.set_index('id_player')

    merged_df = pd.merge(stats_melted, diff_stats_df, left_on=['id_player','stats'], right_on=['id_player','diff_stats'], how='outer')
    stats_df = merged_df.drop(columns='diff_stats')
    return stats_df


def save_to_csv(df, filename):
    # Guardar el DataFrame en un archivo CSV
    df.to_csv(filename, index=True)


# Pipeline function to apply all transformations
def pipeline(df, output_dir):
    player_df = create_player_df(df)
    gender_df = create_gender_df(df)
    player_technical_df = create_player_technical_df(df)
    player_abilities_df = create_player_abilities_df(df)
    team_df = create_team_df(df)
    nationality_df = create_nationality_df(df)
    stats_df = create_stats_df(df)

    # Save each DataFrame into a CSV file
    save_to_csv(player_df, os.path.join(output_dir, "player_data.csv"))
    save_to_csv(gender_df, os.path.join(output_dir, "gender_data.csv"))
    save_to_csv(player_technical_df, os.path.join(output_dir, "player_technical_data.csv"))
    save_to_csv(player_abilities_df, os.path.join(output_dir, "player_abilities_data.csv"))
    save_to_csv(team_df, os.path.join(output_dir, "team_data.csv"))
    save_to_csv(nationality_df, os.path.join(output_dir, "nationality_data.csv"))
    save_to_csv(stats_df, os.path.join(output_dir, "stats_data.csv"))


FILE_PATH = os.path.join('extraction', 'raw_data', 'fc25players_10_21_2024.csv')
df = pd.read_csv(FILE_PATH)

output_directory = os.path.join('transformation', 'transformed_data') 
os.makedirs(output_directory, exist_ok=True)

# Apply the pipeline to raw data
pipeline(df, output_directory)