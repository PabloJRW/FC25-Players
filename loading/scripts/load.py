import os
import pandas as pd
from sqlalchemy import create_engine

# 
players = os.path.join('transformation','transformed_data','player_data.csv')
player_abilities = os.path.join('transformation','transformed_data','player_abilities_data.csv')
nationality = os.path.join('transformation','transformed_data','nationality_data.csv')
player_technical = os.path.join('transformation','transformed_data','player_technical_data.csv')    
stats = os.path.join('transformation','transformed_data','stats_data.csv')
team = os.path.join('transformation','transformed_data','team_data.csv') 

players = pd.read_csv(players)
player_abilities = pd.read_csv(player_abilities)
nationality = pd.read_csv(nationality)
player_technical = pd.read_csv(player_technical)
stats = pd.read_csv(stats)
team = pd.read_csv(team)

# Configurar la cadena de conexión para PostgreSQL
usuario = 'postgres'
contraseña = 'base'
host = 'localhost'  # Cambia esto si el servidor no está en local
puerto = '5432'     # Puerto predeterminado para PostgreSQL
base_datos = 'fc25_players'

# Crear la conexión a la base de datos PostgreSQL
engine = create_engine(f'postgresql://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}')

# Guardar el DataFrame en la base de datos
players.to_sql('players', con=engine, if_exists='replace', index=False)
player_abilities.to_sql('abilities', con=engine, if_exists='replace', index=False)
stats.to_sql('stats', con=engine, if_exists='replace', index=False)
team.to_sql('teams', con=engine, if_exists='replace', index=False)
nationality.to_sql('nationality', con=engine, if_exists='replace', index=False)
player_technical.to_sql('technical', con=engine, if_exists='replace', index=False)

# Cerrar la conexión
engine.dispose()
