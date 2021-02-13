import re
import tweepy
from config import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
# view = ["why the hell does it take 30 minutes to find a ride now?"]
sid = SentimentIntensityAnalyzer()
# for sen in view:
#     print(sen)
#     ss = sid.polarity_scores(sen)
#     for k in ss:
#         print('{0}:{1},'.format(k, ss[k]), end='')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


query = '$spy -filter:retweets'

fetchedTweets = tweepy.Cursor(api.search,q = query,lang ="en").items(100)

negWeightScore = 0
neuWeightScore = 0
posWeightScore = 0

weightedTweetDic = {}

for item in fetchedTweets:
    print(item.id)
    print(item.text + 'n/')
    print(item.id)
    print("="*30)
    ss = sid.polarity_scores(item.text)
    for k in ss:
        print('{0}:{1},'.format(k, ss[k]))
    
    print("++++"*30)
    print(item.retweet_count)
    print(item.favorite_count)
    print("-"*20)
    sum = 1 + item.retweet_count + item.favorite_count
    #weighted score for current tweet
    comScore = ss['compound']
    if comScore < -0.05:
        negWeightScore +=comScore
              
    elif comScore> 0.30:
        posWeightScore+=comScore
    else:
        neuWeightScore+=comScore
    weightedTweetDic[item.id]= sum

print("neg" + str(negWeightScore))
print("neu" + str(neuWeightScore))
print("pos" + str(posWeightScore))
print(weightedTweetDic)





        