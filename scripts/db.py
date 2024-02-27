import sys
import mariadb

lol = 'lol'

try:
    conn = mariadb.connect(
        user="root",
        password="Wolfie01",
        host="localhost",
        database="sensor_data" 
    )
    
except mariadb.Error as e:
    print(f"Error: {e}")
    sys.exit(1)

cur = conn.cursor()
