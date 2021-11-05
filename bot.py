import tweepy
CONSUMER_KEY = 'zkbYgY2KH2sSZDzlJeAPtxoTU'
CONSUMER_SECRET = 'rUUx3VJZ32evg6Tw079tY573OfzmWr7qlYVO1g7fFz3O6cGGfF'
ACCESS_KEY = '1456598880754278401-hmCWvGAnJ40QcN64ny4KcvmazgmrPj'
ACCESS_SECRET = 'PSj6ce22Ws9D6iT7Aj2uorVIGLmW1NiT9DJbceJ6SuUxj'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://countrymeters.info/en/World'
while True:
 reponse = requests.get(url)
 soup = BeautifulSoup(reponse.text,"html.parser")
 item=soup.find('td')
 population=item.div.text
 time.sleep(15)
 tweet = 'The current world population is %s' %(population)
 api.update_status(tweet)#
