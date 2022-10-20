import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password2022"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE phrasedb")