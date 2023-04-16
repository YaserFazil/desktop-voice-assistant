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


cursor.execute("SELECT * FROM info")
results = cursor.fetchall()
print(results[0][0])

ASSISTANT_NAME = "Jarvis"
OWNER_NAME = results[0][0]
CITY_NAME = results[0][4]
