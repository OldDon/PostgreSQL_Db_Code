import psycopg2

# Update connection string information obtained from the portal
host = "psql-server-azure.postgres.database.azure.com"
user = "dave@psql-server-azure"
dbname = "psql-server-azure.postgres.database.azure.com"
password = "k79hH3*iuWe1"
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("CREATE TABLE inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print ("Inserted 3 rows of data")

# Cleanup
conn.commit()
cursor.close()
conn.close()