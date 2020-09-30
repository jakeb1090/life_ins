import sqlite3

connection = sqlite3.connect('todo.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32)
    );"""
)
connection.commit()
    
cursor.execute(    
    """CREATE TABLE tasks(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        task VARCHAR(16),
        due_date VARCHAR(8)
    );"""
)

connection.commit()
cursor.close()
connection.close()
