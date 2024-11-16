import sqlite3
connection = sqlite3.connect("HM9.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE weather (date TEXT, temperature REAL);")
connection.commit()
connection.close()