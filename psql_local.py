import psycopg2

# Set variables for connection string
host = "localhost"
user = "postgres"
dbname = "postgres"
password = "admin"

# Construct the connection string
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

def reread_data():
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    # Display the updated table
    for row in rows:
        print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
# reread_data()

# drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventory;")
print ("Finished dropping table (if existed)")

# Create table
cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER, weight REAL);")
print ("Finished creating table")

# Update/Add to table
cursor.execute("insert into inventory (name, quantity, weight) values (%s, %s, %s);", ("banana", 150, 34.1))
cursor.execute("insert into inventory (name, quantity, weight) values (%s, %s, %s);", ("orange", 154, 110.41))
cursor.execute("insert into inventory (name, quantity, weight) values (%s, %s, %s);", ("apple", 100, 60.18))
print ("inserted 3 rows of data")
reread_data()

# Update a data row in the table
cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (200, "banana"))
print ("Updated 1 row of data")
reread_data()

# Delete data row from table
cursor.execute("DELETE FROM inventory WHERE name = %s;", ("orange",))
print ("Deleted 1 row of data")
reread_data()

# Fetch all rows from table
cursor.execute("SELECT * FROM inventory;")
rows = cursor.fetchall()

# Print all rows
for row in rows:
    print ("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Connection closed")