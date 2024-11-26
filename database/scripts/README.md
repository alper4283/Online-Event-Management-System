## Start a database on your local 
psql -U postgres -c "CREATE DATABASE eventlink;"

## Load from the dump
first get to database/sql/ then
psql -U postgres -d eventlink < database_dump.sql

---------------------------------------------------------------------------------------------


1) Create a Virtual Environment

python3 -m venv venv
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2) Activate the Virtual Environment

# For Linux/MacOS
source venv/bin/activate  
# On Windows:
 venv\Scripts\activate
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3) Install Dependencies

pip install -r requirements.txt
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4) Run the Script

python databasePopulationScript.py
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------