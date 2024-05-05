import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",          # Hostname
    user="sampada",      # Your MySQL username
    password="Sampada@123",  # Your MySQL password
    database="llp"   # Your MySQL database name
)

# Check if the connection is successful
if conn.is_connected():
    print("Connected to MySQL database")

# Perform database operations here

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query
cursor.execute("SELECT * FROM user_languages")

# Fetch the results
result = cursor.fetchall()
for row in result:
    print(row)

# Close cursor
cursor.close()

