from flaskr.db import get_connection

print("Connecting...")

conn = get_connection()

print("Connected!")

cur = conn.cursor()
cur.execute("SELECT 1")

print(cur.fetchone())

cur.close()
conn.close()
