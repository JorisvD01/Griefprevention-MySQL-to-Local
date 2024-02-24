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

mycursor.execute("SELECT * FROM griefprevention_playerdata")

myresult = mycursor.fetchall()

for x in myresult:
  with open(f'PlayerData/{x[0]}','w') as file:
    file.write(f"\n{x[2]}\n{x[3]}\n\n")