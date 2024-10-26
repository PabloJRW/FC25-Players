import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Paths to dataframes
players = os.path.join('transformation','transformed_data','player_data.csv')
player_abilities = os.path.join('transformation','transformed_data','player_abilities_data.csv')
nationality = os.path.join('transformation','transformed_data','nationality_data.csv')
player_technical = os.path.join('transformation','transformed_data','player_technical_data.csv')    
stats = os.path.join('transformation','transformed_data','stats_data.csv')
team = os.path.join('transformation','transformed_data','team_data.csv') 


# Loading all the dataframes
players = pd.read_csv(players)
player_abilities = pd.read_csv(player_abilities)
nationality = pd.read_csv(nationality)
player_technical = pd.read_csv(player_technical)
stats = pd.read_csv(stats)
team = pd.read_csv(team)


# Load the environment variables from .env file
load_dotenv()

# Invoke credentials
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Create connection to PostgreSQL database
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Save the Dataframes into the database
players.to_sql('players', con=engine, if_exists='replace', index=False)
player_abilities.to_sql('abilities', con=engine, if_exists='replace', index=False)
stats.to_sql('stats', con=engine, if_exists='replace', index=False)
team.to_sql('teams', con=engine, if_exists='replace', index=False)
nationality.to_sql('nationality', con=engine, if_exists='replace', index=False)
player_technical.to_sql('technical', con=engine, if_exists='replace', index=False)

# Close connection
engine.dispose()
