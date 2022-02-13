# Levy lab Computers' status collection script

## Purpose

- Collecting all Levy Lab's Windows-based computer's information(IP v4, Mac address, Operating System version and etc.)
- Upload to a PostgreSQL database

## Usage

- A Python script to collect and filter necessary PC status information.
- Install Python on every PC if haven't done yet.
- An AutoStart batch to call python script and pip install psycopg2 for connecting to PostgreSQL database.
- The Python script upload data to PostgreSQL database.
- If no internet connection currently, save it at local and upload to the database later.
