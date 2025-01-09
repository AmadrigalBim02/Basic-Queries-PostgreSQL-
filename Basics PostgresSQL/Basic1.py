import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="123",
    port=5432
)
cur = conn.cursor()

# Create the car_inventory table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS car_inventory (
        id INT PRIMARY KEY,
        brand VARCHAR(255),
        year INT,
        module VARCHAR(255)
    );
""")

# Insert data into car_inventory table
cur.execute("""
    INSERT INTO car_inventory (id, brand, year, module) VALUES
        (1, 'Tesla', 2017, 'Hatchback'),
        (2, 'Honda', 2010, 'Hatchback'),
        (3, 'Toyota', 2011, 'Sedan'),
        (4, 'Ford', 2000, 'Coupe'),
        (5, 'BMW', 2013, 'Hatchback')
    ON CONFLICT (id) DO NOTHING; 
""")

# Commit changes to the database
conn.commit()

# Retrieve all cars
cur.execute("SELECT * FROM car_inventory;")
print("All cars:")
print(cur.fetchall())
print()

# Retrieve only 'brand' and 'year' of cars
cur.execute("SELECT brand, year FROM car_inventory;")
print("Brand and year of all cars:")
print(cur.fetchall())
print()

# Retrieve cars with 'year' greater than or equal to 2010
cur.execute("SELECT * FROM car_inventory WHERE year >= 2010;")
print("Cars with year >= 2010:")
print(cur.fetchall())
print()

# Retrieve cars that are not Hatchbacks
cur.execute("SELECT * FROM car_inventory WHERE module != 'Hatchback';")
print("Cars that are not Hatchbacks:")
print(cur.fetchall())
print()

# Retrieve cars manufactured by either Tesla or BMW
cur.execute("SELECT * FROM car_inventory WHERE brand IN ('Tesla', 'BMW');")
print("Cars manufactured by Tesla or BMW:")
print(cur.fetchall())
print()

# Retrieve cars with 'year' between 2005 and 2015
cur.execute("SELECT * FROM car_inventory WHERE year BETWEEN 2005 AND 2015;")
print("Cars with year between 2005 and 2015:")
print(cur.fetchall())
print()

# Count the total number of cars
cur.execute("SELECT COUNT(*) FROM car_inventory;")
print("Total number of cars:")
print(cur.fetchone())
print()

# Find the earliest and latest manufacturing year
cur.execute("SELECT MIN(year) AS earliest_year, MAX(year) AS latest_year FROM car_inventory;")
print("Earliest and latest manufacturing year:")
print(cur.fetchone())
print()

# Count the number of cars by module type
cur.execute("SELECT module, COUNT(*) AS count FROM car_inventory GROUP BY module;")
print("Number of cars by module type:")
print(cur.fetchall())
print()

# Retrieve cars sorted by 'year' in ascending order
cur.execute("SELECT * FROM car_inventory ORDER BY year ASC;")
print("Cars sorted by year (ascending):")
print(cur.fetchall())
print()

# Retrieve cars sorted by 'brand' in descending order
cur.execute("SELECT * FROM car_inventory ORDER BY brand DESC;")
print("Cars sorted by brand (descending):")
print(cur.fetchall())
print()

# Update Tesla's module to 'Sedan'
cur.execute("UPDATE car_inventory SET module = 'Sedan' WHERE brand = 'Tesla';")
conn.commit()
print("Updated Tesla's module to 'Sedan'.")

# Increase the 'year' for all cars by 1
cur.execute("UPDATE car_inventory SET year = year + 1;")
conn.commit()
print("Increased year of all cars by 1.")

# Retrieve all cars to see updates
cur.execute("SELECT * FROM car_inventory;")
print("All cars after updates:")
print(cur.fetchall())
print()

# Delete cars older than 2010
cur.execute("DELETE FROM car_inventory WHERE year < 2010;")
conn.commit()
print("Deleted cars older than 2010.")

# Delete all BMW cars
cur.execute("DELETE FROM car_inventory WHERE brand = 'BMW';")
conn.commit()
print("Deleted all BMW cars.")

# Retrieve all cars to see deletions
cur.execute("SELECT * FROM car_inventory;")
print("All cars after deletions:")
print(cur.fetchall())
print()

# Retrieve cars and categorize them as 'Old' (year < 2010) or 'New' (year >= 2010)
cur.execute("""
    SELECT brand, year,
    CASE
        WHEN year < 2010 THEN 'Old'
        ELSE 'New'
    END AS category
    FROM car_inventory;
""")
print("Cars categorized by 'Old' or 'New':")
print(cur.fetchall())
print()

# Retrieve the module with the most cars
cur.execute("""
    SELECT module, COUNT(*) AS count
    FROM car_inventory
    GROUP BY module
    ORDER BY count DESC
    LIMIT 1;
""")
print("Module with the most cars:")
print(cur.fetchone())
print()


# Create a temporary table for cars manufactured after 2010
cur.execute("""
    CREATE TEMP TABLE temp_car_inventory AS
    SELECT * FROM car_inventory WHERE year > 2010;
""")
print("Created temporary table for cars manufactured after 2010.")

# Retrieve data from the temporary table
cur.execute("SELECT * FROM temp_car_inventory;")
print("Cars in temporary table:")
print(cur.fetchall())
print()


# Retrieve the first 2 cars (limit)
cur.execute("SELECT * FROM car_inventory LIMIT 2;")
print("First 2 cars:")
print(cur.fetchall())
print()

# Retrieve the next 2 cars (offset)
cur.execute("SELECT * FROM car_inventory LIMIT 2 OFFSET 2;")
print("Next 2 cars:")
print(cur.fetchall())
print()

# Convert rows to JSON format
cur.execute("""
    SELECT json_agg(row_to_json(car_inventory))
    FROM car_inventory;
""")
print("Cars in JSON format:")
print(cur.fetchone())
print()

# Close the cursor and connection
cur.close()
conn.close()
