# description : This is a sentiment propgram that parses the tweets fetched from Twitter using Python

# import the libraries
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Load the data
from google.colab import files
uploaded = files.upload()

# Get the data
log = pd.read_csv('Login.csv')

# Twitter API credentials
consumerKey = log['key'][0]
consumerSecret = log['key'][1]
accessToken = log['key'][2]
accessTokenSecret = log['key'][3]

authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret)

# Create the API object while passing in the auth information
api = tweepy.API(authenticate, wait_on_rate_limit = True)


# Extract 100 tweets from the twitter user
posts = api_timeline(screen_name = "BillGates", count = 100, lang = "en", tweet_mode = "extended")

# Print the last 5 tweets from the account 
print("Show the 5 recent tweets: \n")
i = i + 1

# Create a dataframe with a column called Tweets
df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])

# Show the first 5 rowa of data
df.head()

# Clean the text

# Create a function to clean the tweets
def cleanTxt(text):
  text = re.sub(r'@[A-Za-z0-9]'; '', text) # Removed @mentions
  text = re.sub(r'#', '', text) #removing the '#' symbol
  text = re.sub(r'RT[\s]+', '', text) # Remove the RT
  text = re.sub(r'https?:\/\/\S+', '', text) # Remove the hyper link

  return text

  df['Tweets'] = df['Tweets'].apply(cleanTxt)

  #Show the cleaned text
  df
  
# Create a function to get the subjectivity
def getSubjectivity(text):
  return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity(text):
  return TextBlob(text).sentiment.polarity

# Create twi new columns
df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolrity)

# Show the new dataframe with the new columns
  

