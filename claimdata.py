import mysql.connector
import yaml
import json

with open('credentials.json','r') as file:
    data = json.load(file)

mydb = mysql.connector.connect(
  host=data['host'],
  user=data['user'],
  password=data['password'],
  database=data['database']
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM griefprevention_claimdata")

myresult = mycursor.fetchall()

for x in myresult:

    data = {
          'Lesser Boundary Corner':x[2],
          'Greater Boundary Corner': x[3],
          'Owner': x[1],
          'Builders': [uuid for uuid in x[4].split(';')[:-1]],
          'Containers': [uuid for uuid in x[5].split(';')[:-1]],
          'Accessors': [uuid for uuid in x[6].split(';')[:-1]],
          'Managers': [uuid for uuid in x[7].split(';')[:-1]],
          'Parent Claim ID': x[9],
          'inheritNothing': False if x[8] == 0 else True
    }

    with open(f'Claimdata/{x[0]}.yml','w') as f:
      yaml.dump(data,f,sort_keys=False)