import re
import tweepy
from config import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime,timedelta

def twitteranalyze(ticker:str) -> list:
    yestoday = datetime.now().strftime('%Y-%m-%d')
    
    sid = SentimentIntensityAnalyzer()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)


    query = '$' + ticker + ' -filter:retweets'

    fetchedTweets = tweepy.Cursor(api.search,q = query,since = yestoday, lang ="en").items(10)

    negWeightScore = 0
    neuWeightScore = 0
    posWeightScore = 0
    weightedTweetDic = {}

    for item in fetchedTweets:
        ss = sid.polarity_scores(item.text)
        
        sum = 1 + item.retweet_count + item.favorite_count
        #weighted score for current tweet
        comScore = ss['compound']
        if comScore < -0.05:
            negWeightScore +=comScore
                
        elif comScore> 0.30:
            posWeightScore+=comScore
        else:
            neuWeightScore+=comScore
        weightedTweetDic[item.id]= comScore


    weightedTweetDic_= sorted(weightedTweetDic.items(), key=lambda x: x[1], reverse=True)

    return [[negWeightScore,neuWeightScore,posWeightScore],weightedTweetDic_]



if __name__ == '__main__':
    ans = twitteranalyze('$TLRY')
    print(ans)
    



        