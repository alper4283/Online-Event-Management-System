# EventLink Database Setup Guide Notes:

This guide will walk you through setting up the EventLink project. Follow the steps below to create a database, load data, set up a virtual environment, and run the script to populate the database. If you want to get the latest version of the database instance just following the first part of the guide is sufficent.

## 1.1 Create the Database For Linux

First, create a new database named eventlink using PostgreSQL.

```bash
psql -U postgres -c "CREATE DATABASE eventlink;"
```

### Load Data from the Dump

To load data into the eventlink database from a dump file, first navigate to the database/sql/ directory, then run:

```bash
psql -U postgres -d eventlink < database_dump.sql
```

or

```bash
sudo -u postgres psql -d eventlink < database_dump.sql
```

## 1.2 Create the Database For Windows

First, create a new database named eventlink using PostgreSQL.

```bash
psql -U postgres -c "CREATE DATABASE eventlink;"
```

To load data into the eventlink database from a dump file, first navigate to the database/sql/ directory, then run:

```bash
psql -U postgres -d eventlink -f database_dump.sql
```


# If You Want To Populate The Database From Scratch
(If you don't want to populate the database from scratch you can omit this part of the README.md file.)

## 2. Set Up a Virtual Environment

Create a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
```

### Activate the Virtual Environment

Linux/MacOS:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

## 3. Install Dependencies

Once the virtual environment is activated, install the project dependencies.

```bash
pip install -r requirements.txt
```

## 4. Run the Script to Populate the Database

Run the following script to populate the database with necessary data.

```bash
python databasePopulationScript.py
```
