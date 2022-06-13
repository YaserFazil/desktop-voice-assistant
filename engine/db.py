from ast import For
from importlib.resources import path
import json
from multiprocessing import connection
from re import I
import sqlite3
from unittest import result
from unittest.mock import patch
import numpy as np
from requests import delete

connection = sqlite3.connect('assistant.sqlite')
cursor = connection.cursor()

# query = "CREATE TABLE IF NOT EXISTS info(name VARCHAR(100), designation VARCHAR(50),mobileno VARCHAR(40), email VARCHAR(200), city VARCHAR(300))"
# cursor.execute(query)

# query = "DROP TABLE phonebook"
# cursor.execute(query)

# cursor.execute(
#     '''INSERT INTO info VALUES ('digambar', 'CSE Student', '7620464305', 'chaudharidigambar52002@gmail.com','Adawad')''')
# connection.commit()

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

query = "babu bhai"

# cursor.execute(
#     "SELECT mobileno FROM phonebook WHERE name='%s'" % query.strip())


# if len(results) != 0:
#     # speak("Calling ", query)
#     for i in results:
#         print(i)


# def personalInfo():
#     cursor.execute("SELECT * FROM sys_command")
#     results = cursor.fetchall()
#     # print(data)
#     return results[0]


# print(personalInfo())


# def updatePersonalInfo(name, desiganation, mobileno, email, city):
#     cursor.execute('''UPDATE info SET name=?, designation=?, mobileno=?, email=?, city=? ''',
#                    (name, desiganation, mobileno, email, city))
#     connection.commit()


# updatePersonalInfo('jojo', 'CSE Student', '7620464305',
#                    'chaudharidigambar52002@gmail.com', 'pune')


# def addSysCommand(key, value):
#     cursor.execute(
#         '''INSERT INTO sys_command VALUES (?, ?)''', (key, value))
#     connection.commit()


# addSysCommand('yellow', 'pink')
