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
import time
url = 'https://countrymeters.info/en/World'
population = '0,0'



while True:
 population_yesterday = population
 population_ysplit = population_yesterday.split(',')
 population_yesterday_end = population_ysplit[-2]+population_ysplit[-1]
 reponse = requests.get(url)
 soup = BeautifulSoup(reponse.text,"html.parser")
 item=soup.find('td')
 population=item.div.text
 populationsplit = population.split(',')
 pop_end = populationsplit[-2] + populationsplit[-1]
 difference = int(pop_end) - int(population_yesterday_end) 
 if difference > 10000:
   difference = 0
 current_time = time.time()
 date = time.ctime(current_time)
 tweet = 'As of %s, the current world population is %s(+%s).' %(date,population,difference)
 api.update_status(tweet)
 time.sleep(30)
