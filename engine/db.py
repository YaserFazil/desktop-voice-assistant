from ast import For
from importlib.resources import path
from multiprocessing import connection
import sqlite3
from unittest import result
from unittest.mock import patch

connection = sqlite3.connect('assistant.sqlite')
cursor = connection.cursor()

# query = "CREATE TABLE IF NOT EXISTS phonebook(name VARCHAR(100), mobileno VARCHAR(40), email VARCHAR(200), address VARCHAR(300))"
# cursor.execute(query)

# query = "DROP TABLE phonebook"
# cursor.execute(query)

cursor.execute(
    '''INSERT INTO phonebook VALUES ('digambar', '7620464305', 'digambarchaudhari425303@gmail.com', 'Adawad')''')
connection.commit()

# cursor.execute("DELETE  FROM hospitals")
# connection.commit()


# cursor.execute("DELETE from sys_command WHERE name='notepad' ")
# connection.commit()
# query = '  notepad  '
# car = query.strip()
# print(query.strip())
# cursor.execute("SELECT path FROM sys_command WHERE name='%s'" % query)
# results = cursor.fetchall()
# flag = results[0]
# path = flag[0]
# print(type(path))
# print(repr(path))

# cursor.execute(
#     "SELECT mobileno FROM phonebook WHERE name='%s'" % query.strip())
# results = cursor.fetchall()
# if len(results) != 0:
#     # speak("Calling ", query)
#     for i in results:
#         print(i)
