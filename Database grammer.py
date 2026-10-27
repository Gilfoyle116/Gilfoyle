import sqlite3

# create database connection   conn is cursor
conn = sqlite3.connect("novels1.db")

# create cursor      cursor object is use to execute sql sentences
cursor = conn.cursor()


# create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        body TEXT NOT NULL
    )
''')

# Adding data
sql = "INSERT INTO users(name, age) VALUES('Gilfoyle', 19)"
cursor.execute(sql)
conn.commit()

# Researching all data
sql = "SELECT * FROM users"
cursor.execute(sql)
print(cursor.fetchall())

# Researching data according to certain conditions
sql = "SELECT * FROM users WHERE name='Gilfoyle'"
cursor.execute(sql)
print(cursor.fetchall())

# Updating data
sql = "UPDATE users SET name = 'Richard' WHERE id = 1"
cursor.execute(sql)
conn.commit()

# Deleting data
sql = "DELETE FROM users WHERE id = 2"
cursor.execute(sql)
conn.commit()

# Closing connection
cursor.close()
conn.close()