import mysql.connector
import json

with open('credentials.json', 'r') as file:
    data = json.load(file)

mydb = mysql.connector.connect(
    host=data['host'],
    user=data['user'],
    password=data['password'],
    database=data['database']
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM griefprevention_schemaversion")

myresult = mycursor.fetchone()

with open('_schemaVersion','w') as file:
  file.write(str(myresult[0]))