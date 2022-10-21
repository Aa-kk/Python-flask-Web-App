import mysql.connector
import requests
import yaml
import variables

mydb = mysql.connector.connect(
    host=variables.host,
    user=variables.user,
    password=variables.password,
    database=variables.database
    )

mycursor = mydb.cursor()

mycursor.execute("Select * from tech_phrases")

for x in mycursor:
    print(x)