# Sentiment Analysis for tweets regarding trump
import tweepy
from textblob import *
import csv

# Authenticating with twitter API
consumer_key = 'OAisHq9oOvq6IRL17uu9mnCyG'
consumer_secret = 'hLug1NJiHQWECaYhTDg8FqZGEzwytcgG4DD3TdHZgJZ9AMhr5v'
access_token = '96994140-db6pLlmCjAt6RGtCFHJhSq8k6wfEUeiu3iAHuAIZJ'
access_token_secret = '8PD7XVsC339JW6uGrpkZFrcb6xhm5ZP0Oa0fyvTUcU4We'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

# Writing the results into a CSV file

with open('tweets.csv', 'wb') as csvfile:
    for count, tweet in enumerate(public_tweets, 1):
        # Sentiment analysis
        analysis = TextBlob(tweet.text)
        label = "Positive" if analysis.sentiment[0] > 0 else "Negative"
        temp = "{}. {} {}".format(count, label, tweet.text.encode('utf8'))
        csvfile.write(temp)
        csvfile.write('\n')
