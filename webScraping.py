from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import math
import string
import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port': '3306',
  'database': 'nba',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)

def insertCSV(i, name, position, height, weight):
    with open('players.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([i, name, position, height, weight])

def insertMySQL(i, name, position, height, weight):
    mycursor = link.cursor()
    sql = "INSERT INTO players (id, name, position, height, weight) VALUES (%s, %s, %s, %s, %s)"
    val = (i, name, position, height, weight)
    mycursor.execute(sql, val)
    link.commit()


letters = list(string.ascii_lowercase)
i = 0
for letter in letters:
    try:
        quote_page = 'https://www.basketball-reference.com/players/'+letter+'/'
        print('procesando letra '+letter)
        page = urlopen(quote_page).read()
        soup = BeautifulSoup(page, 'html.parser')
        players = soup.find('table', attrs={'id': 'players'})
        tbody = players.find('tbody')
        trs = tbody.find_all('tr')
        for player in tbody.find_all('tr'):
            try:
                name = player.find('th', attrs = {'data-stat': 'player'}).text.encode('utf-8')
                position = player.find('td', attrs = {'data-stat': 'pos'}).text.encode('utf-8')
                heightLB = player.find('td', attrs = {'data-stat': 'height'}).text.split("-")
                height = int(math.ceil(int(heightLB[0]) * 30.48 + int(heightLB[1]) * 2.54))
                weightP = player.find('td', attrs = {'data-stat': 'weight'}).text
                i = i + 1
                if(weightP != ''):
                    weight = int(math.ceil(int(weightP) / 2.205))
                else:
                    weight = 0
                insertCSV(i, name, position, height, weight)
                insertMySQL(i, name, position, height, weight)
            except AttributeError as e:
                print (e)
    except urllib2.HTTPError:
        print ('url no existe')


