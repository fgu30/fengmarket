
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
view = ["My Top Stock Picks For 2021: $AAPL (Apple) 133.11 $AMZN (Amazon) 3262.66 $TSLA (Tesla Motors, Inc.) 706.59 $NIO (Nio Inc.) 48.80 $PLTR (Palantir) 23.57 $JMIA (Jumia Technologies AG) 40.47 $SHOP  1135.08 $SQ 217.93 $CHWY 90 $TDOC 200.18 $PLUG 33.98 $FCEL  11.18 $BLNK 42.72"]
sid = SentimentIntensityAnalyzer()
for sen in view:
    print(sen)
    ss = sid.polarity_scores(sen)
    for k in ss:
        print('{0}:{1},'.format(k, ss[k]), end='')
