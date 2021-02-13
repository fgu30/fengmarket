import requests
r = requests.get('https://finnhub.io/api/v1/etf/holdings?symbol=QQQ&token=c0ib9g748v6qfc9dfkd0')
stocks = r.json()['holdings']

for stock in stocks:
    print(stock)
    print("="*30)

