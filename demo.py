from secret import *
import tweepy
from textblob import TextBlob

#All the tokens needed to ACCESS the API
consumer_key, consumer_secret = API_KEY, API_SECRET_KEY
access_token, access_token_secret = ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Retrieve Tweets
public_tweets = api.search('Artificial Intelligence')

#Print tweets to console 
for tweet in public_tweets:
    print(tweet.text +'\n')

    #textblob is used to analyze the popularity and subjectivity of tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
