# FC25 Players: ETL Project

This project involves the extraction, transformation, and loading (ETL) of player data from the official FC25 game website using its API. The data is then transformed and loaded into a PostgreSQL database for analysis and reporting.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [ETL Steps](#etl-steps)
6. [Configuration](#configuration)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview
The main goal of this project is to gather data on FC25 players, transform it for proper structure and analysis, and store it in a PostgreSQL database. The data is extracted via API, cleaned and transformed according to defined rules, and then loaded  into the database.

### Key Features
- Extract data from the FC25 API.
- Cleans and transforms the data to ensure consistency.
- Loads the data into a PostgreSQL database.
- Splits the main table into normalized tables.
- Each task is executed individually to allow for modular control of the ETL process.

## Requirements
To run this project, you need:
- Python 3.8 or higher
- PostgreSQL 17 or higher
- The following Python libraries
  - `requests`
  - `pandas`
  - `sqlalchemy`
  - `psycopg2`
 
## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:PabloJRW/FC25-Players-ETL.git
   cd FC25-Players-ETL
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the PostgreSQL database:
- Create a new PostgreSQL database.
- Update the database configuration in the project ([see Configuration section](#configuration)).

## Usage
Each step of the ETL process needs to be run individually. Follow these steps to execute each task:
1. **Extract data:**
```bash
python extraction/scripts/extract.py
```

2. **Transform data:**
```bash
python transformation/scripts/extract.py
```

3. **Load data to the database:**  
```bash
python loading/scripts/load.py
```

Make sure to run these scripts in the correct order for the data to be properly extracted, transformed, and loaded.

## ETL Steps
1. **Extraction:**
    - Retrieves player data from the FC25 API in JSON format.
2. **Transformation:**
    - Cleans the data, handles missing values, and converts data types.
    - Applies specific transformation rules to prepare the data for the database.
3. **Loading:**
    - Inserts the transformed data into the PostgreSQL database.

## Configuration

Before running the project, you need to set up your database connection and API configuration. Create a `.env` file in the root directory of the project and add the following settings:

```plaintext
DB_HOST=your_db_host          # The host of your PostgreSQL database
DB_PORT=5432                  # The port for your PostgreSQL database
DB_NAME=your_db_name          # The name of your PostgreSQL database
DB_USER=your_db_user          # Your PostgreSQL username
DB_PASSWORD=your_db_password  # Your PostgreSQL password
```

You can customize these settings according to your environment.

## Project Structure
``` bash
FC25-Players/
├── extraction/                   # Directory for data extraction
│   ├── raw_data/                 # Directory to store raw data extracted from the API
│   └── scripts/                  # Directory containing extraction scripts
│       ├── extract.py            # Script for extracting player data from the API
│       └── extract_stats_list.py  # Script for extracting a list of player statistics
├── transformation/                # Directory for data transformation
│   ├── transformed_data/          # Directory to store transformed data
│   └── scripts/                   # Directory containing transformation scripts
│       └── transformation.py      # Script for transforming raw data into a suitable format
├── loading/                       # Directory for data loading
│   └── scripts/                   # Directory containing loading scripts
│       └── load.py               # Script for loading transformed data into the PostgreSQL database
├── tests/                         # Directory for testing scripts
│   ├── extraction.py              # Test script for verifying extraction functionality
│   └── transformation_test.ipynb  # Jupyter notebook for testing data transformation
├── requirements.txt               # File listing required Python libraries for the project
├── README.md                      # Project documentation providing an overview and instructions
├── .env                           # Database credentials (not included in the repo for security reasons).
└── fc25venv                       # Virtual environment directory for managing project dependencies
```

## Contributing
If you would like to contribute to this project, feel free to submit a pull request or open an issue with suggestions for improvement.

## License
This project is licensed under the MIT License. See the LICENSE file for details.







   
