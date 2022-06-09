from opensea import OpenseaAPI
from dotenv import load_dotenv
import os
import requests
import sqlite3
import datetime

load_dotenv()
api_keys=os.getenv('apikey')
api=OpenseaAPI(api_keys)



url = "https://api.opensea.io/api/v1/collection/boredapeyachtclub/stats"

headers = {
    "Accept": "application/json",
    "X-API-KEY": api_keys
}

response = requests.get(url, headers=headers)
floor_price=response.json()['stats']['floor_price']
# print(floor_price)

conn=sqlite3.connect('baycfloor.db')
c=conn.cursor()
# c.execute('''CREATE TABLE floor_prices(date DATE, price FLOAT)''')

date=datetime.datetime.today()
date=datetime.datetime(date.year, date.month, date.day, date.hour, date.minute)

c.execute('''INSERT INTO floor_prices VALUES(?,?)''', (date, floor_price))
conn.commit()
print(f'Data just added ({date})')