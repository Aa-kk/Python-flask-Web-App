import mysql.connector
import requests
import yaml


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="phrasedb"
)

mycursor = mydb.cursor()

mycursor.execute("Select * from tech_phrases")

for x in mycursor:
    print(x)