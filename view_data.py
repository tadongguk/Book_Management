import sqlite3

# Connect to the database
conn = sqlite3.connect('book.db')
cursor = conn.cursor()

# Function to read and print data from a table
def read_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    print(f"\nData from table {table_name}:")
    # Get column names
    column_names = [description[0] for description in cursor.description]
    print(", ".join(column_names))
    
    # Print data
    for row in rows:
        print(", ".join(map(str, row)))

# List of tables to read
tables = ['authors', 'genres', 'books', 'readers', 'loans']

# Read data from each table
for table in tables:
    try:
        read_table(table)
    except sqlite3.OperationalError as e:
        print(f"Error reading table {table}: {e}")

# Close the connection
conn.close()

print("\nFinished reading data from all tables.")