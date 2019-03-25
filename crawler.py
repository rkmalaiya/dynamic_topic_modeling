import tweepy
import csv
import pandas as pd
import sys

####input your credentials here
access_token = "101973377-Wb4deNtdXdSfsdfoUo7SKVOnHjf8SEZlAJ8s7JAl"
access_token_secret = "GNcU23gzwfRY8BLSUIQmea1SCc9BnZtHGsWPyWwKhgwtq"
consumer_key = "rNQwltpJhYMOVK6NdEPMDNgK7"
consumer_secret = "JZzweIEuGCi4NbY2SvEvvfDw8UyOetVAJ2SY7s6Y7QkTBpGYay"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('data/twitter_data_{}.csv'.format(sys.argv[1]), 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
print("Collecting Data for: #{}".format(sys.argv[1]))
for tweet in tweepy.Cursor(api.search,q="#{}".format(sys.argv[1]),
                           lang="en",
                           since="2010-01-01").items():
    if len(tweet.text.split(':',1)) > 1:
        tweet_text = tweet.text.split(':',1)[1] 
    else:
        continue 
    #print (tweet.created_at, tweet_text)
    csvWriter.writerow([tweet.created_at, tweet_text.encode('utf-8')])
    
csvFile.close()