from secret import *
import tweepy
from textblob import TextBlob
import csv

#All the tokens needed to ACCESS the API
consumer_key, consumer_secret = API_KEY, API_SECRET_KEY
access_token, access_token_secret = ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Retrieve Tweets
public_tweets = api.search('Artificial Intelligence')

#Print tweets to console 
with open('sentiments.csv', 'w', newline='') as csvfile:
    tweetwriter = csv.writer(csvfile, delimiter = ' ', quotechar='|', quoting = csv.QUOTE_MINIMAL)
    tweetwriter.writerow(['Public Tweet', 'Polarity Score', 'Subjectivity Score', 'Positive/Negative', 'Factuality']) #header row

    for tweet in public_tweets:
        print(tweet.text +'\n')

        #textblob is used to analyze the popularity and subjectivity of tweets
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
#        print("")
        polarity = analysis.sentiment[0]
        subjectivity = analysis.sentiment[1]

        if polarity < 0:
            feeling = 'Negative' #Describes the overall sentiment of statement but avoiding sentiment keyword
        elif polarity == 0:
            feeling = 'Neutral'
        elif polarity > 0:
            feeling = 'Positive'

        if subjectivity >= 0.5:
            statement_type = 'Opinion' #Determines the objectivity/subjectivity of statement
        elif subjectivity < 0.5:
            statement_type = 'Factual Report'

        print(f'Overall Sentiment: {feeling}, Factuality: {statement_type}\n')
        tweetwriter.writerow([tweet.text, polarity, subjectivity, feeling, statement_type])
        

#TODO Modify algorithm so that it's more discering of opinion/fact-based news and less binary with sentiment
