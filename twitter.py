import tweepy
import time
import os
from os import environ

API_KEY = environ['API_KEY']
API_SECRET = environ['API_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def retrieve_last_seen_id(file_name):
  f_read = open(file_name, 'r')
  last_seen_id = int(f_read.read().strip())
  f_read.close()
  return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
  f_write = open(file_name, 'w')
  f_write.write(str(last_seen_id))
  f_write.close()
  return

FILE_NAME = 'last_fav_tweet_id.txt'

def fav_tweet():
    print('Tweetssss......')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = "extended")
    for mention in reversed(mentions):
        if not mention:
            return
        print(str(mention.in_reply_to_status_id) + '-Tweet ID ' + mention.full_text, flush=True)
        last_fav_tweet = mention.id
        store_last_seen_id(last_fav_tweet,FILE_NAME)
        print('like and retweet', flush=True)
        try:
          if(mention.in_reply_to_status_id == None):
                api.create_favorite(mention.id)
                api.retweet(mention.id)
              
          else:
              api.create_favorite(mention.in_reply_to_status_id)
              api.retweet(mention.in_reply_to_status_id)
              api.create_favorite(mention.id)
        except:
          continue

while True:
    fav_tweet()
    time.sleep(15)