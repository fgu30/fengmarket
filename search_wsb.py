from psaw import PushshiftAPI
import config
import datetime
import psycopg2
import psycopg2.extras
import re

connection = psycopg2.connect(
    host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor.execute("""
    SELECT * FROM stock
""")
rows = cursor.fetchall()

stocks = {}
for row in rows:
    stocks[row['symbol']] = row['id']


api = PushshiftAPI()

start_time = int(datetime.datetime(2021, 2, 9).timestamp())

submissions = api.search_submissions(after=start_time,
                                     subreddit='wallstreetbets',
                                     filter=['url', 'author', 'title', 'subreddit'])


    

for submission in submissions:
    words = submission.title
    pattern = re.compile(r'(?<![A-Z]\s)\b[A-Z]+\b(?!\s[A-Z])')
    
    cashtags_ = pattern.findall(words)

    words= ['A','I','DD','HOLD','BUY'] 

    cashtags = [" ".join([w for w in t.split() if not w in words]) for t in cashtags_]
    
    if len(cashtags) > 0:
        print(cashtags)
        print(submission.title)

        for cashtag in cashtags:
            if cashtag in stocks:
                submitted_time = datetime.datetime.fromtimestamp(
                    submission.created_utc).isoformat()

                try:
                    cursor.execute("""
                        INSERT INTO mention (dt, stock_id, message, source, url)
                        VALUES (%s, %s, %s, 'wallstreetbets', %s)
                    """, (submitted_time, stocks[cashtag], submission.title, submission.url))

                    connection.commit()
                except Exception as e:
                    print(e)
                    connection.rollback()
