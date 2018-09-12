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

# drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventory;")
print ("Finished dropping table (if existed)")

# Create table
cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
print ("Finished creating table")

cursor.execute("insert into inventory (name, quantity) values (%s, %s);", ("banana", 150))
cursor.execute("insert into inventory (name, quantity) values (%s, %s);", ("orange", 154))
cursor.execute("insert into inventory (name, quantity) values (%s, %s);", ("apple", 100))
print ("inserted 3 rows of data")

# # Drop previous table of same name if one exists
# cursor.execute("CREATE TABLE inventory (name, quantity) VALUES  ("banana", 150);")
# cursor.execute("INSERT INTO inventory (name, quantity) VALUES ("orange", 154);")
# cursor.execute("INSERT INTO inventory (name, quantity) VALUES  ("apple", 100);")
# print ("Inserted 3 rows of data")

# Start block of code to read and display all data within db
# Fetch all rows from table
cursor.execute("SELECT * FROM inventory;")
rows = cursor.fetchall()

# Print all rows
for row in rows:
    print ("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
# End block of code to read and display all data within db

# Start block of code to update a single row
# Update a data row in the table
cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (200, "banana"))
print ("Updated 1 row of data")
# End block of code that updates a single row

# To check update, fetch data again and print the rows again
# Fetch all rows from table
cursor.execute("SELECT * FROM inventory;")
rows = cursor.fetchall()
# Print all rows
for row in rows:
    print ("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
# End block of code to read and display all data within db

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Connection closed")