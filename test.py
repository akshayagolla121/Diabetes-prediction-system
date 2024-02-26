import sqlite3
import pandas as pd

# Create the database connection
conn = sqlite3.connect('diabetes.db')

# Create a cursor object
cur = conn.cursor()

# Define the CREATE TABLE query
create_table_query = '''
CREATE TABLE IF NOT EXISTS DIABETES (
    PREGNANCIES INT,
    GLUCOSE INT,
    BLOODPRESSURE INT,
    SKINTHICKNESS INT,
    INSULIN INT,
    BMI FLOAT,
    DIABETESPREDIGREEFUNCTION FLOAT,
    AGE INT,
    PREDICTED_RES INT
);
'''

# Execute the CREATE TABLE query
cur.execute(create_table_query)

# Read the data from the CSV file
data = pd.read_csv('diabetes.csv')  
# Write the data to the 'DIABETES' table in the SQLite database
data.to_sql('DIABETES', conn, if_exists='replace', index=False)
#conn.execute('DROP TABLE DIABETES')
# Commit the changes and close the connection
conn.commit()
conn.close()
