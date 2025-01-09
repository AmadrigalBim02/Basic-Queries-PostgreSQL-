# Basic-Queries-PostgreSQL-
Overview
This Python script demonstrates the use of the psycopg2 library to interact with a PostgreSQL database. It manages a car inventory database, showcasing various database operations, including creation, insertion, querying, updating, deletion, and advanced queries.

Key Features
Database Connection:

Establishes a connection to the PostgreSQL database using psycopg2.
Connects to a database named postgres with user credentials.
Table Creation:

Creates a table car_inventory with the following columns:
id (Primary Key): Unique identifier for each car.
brand: The brand of the car (e.g., Tesla, Honda).
year: The manufacturing year of the car.
module: The type/model of the car (e.g., Hatchback, Sedan).
Data Insertion:

Inserts five initial car records into the car_inventory table.
Ensures duplicate entries are avoided using ON CONFLICT.
Querying Data:

Retrieves all cars and performs a variety of queries, including:
Cars with year >= 2010.
Cars that are not Hatchbacks.
Cars by specific brands (e.g., Tesla, BMW).
Cars sorted by year or brand.
Count of cars by type or year range.
Updating Data:

Updates specific attributes, such as changing Tesla’s module to Sedan.
Increments the year of all cars by 1.
Deleting Data:

Deletes cars older than 2010.
Deletes all cars of a specific brand (e.g., BMW).
Advanced Queries:

Categorizes cars as 'Old' or 'New' based on the year.
Identifies the module with the most cars.
Converts car records into JSON format for structured data representation.
Temporary Tables:

Creates a temporary table for cars manufactured after 2010.
Pagination:

Retrieves data using LIMIT and OFFSET for pagination.
How to Use
Pre-Requisites:

Ensure PostgreSQL is installed and running.
Create a database named postgres if it doesn't already exist.
Install psycopg2 using:
bash
Copy code
pip install psycopg2
Run the Script:

Save the script to a file (e.g., car_inventory.py).
Execute the script:
bash
Copy code
python car_inventory.py
Database Setup:

The script automatically creates the car_inventory table if it doesn’t exist.
Initial car data is inserted only if not already present.
Output
The script outputs the results of various operations to the console, including:

All cars in the database.
Filtered and categorized cars.
Cars sorted by specific criteria.
Summary statistics, such as car counts and year ranges.
Customization
You can modify the script to:

Add more car records.
Perform additional queries or transformations.
Integrate with external data sources or APIs.
Error Handling
The script does not include robust error handling but assumes the database connection and table creation succeed. For production use, add try-except blocks to handle exceptions gracefully.

This script is a practical example of working with relational databases in Python and serves as a foundational tool for managing and analyzing structured data in PostgreSQL.
