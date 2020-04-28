import tweepy

from secrets import *
from tweet_builder import TweetBuilder

if __name__ == "__main__":
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)  
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)  
  api = tweepy.API(auth)

  tweet_builder = TweetBuilder()
  
  api.update_status(tweet_builder.build_tweet())