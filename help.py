from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&symbols=ghst"


session = Session()
# session.headers.update(headers)

try:
  response = session.get(url)
  data = json.loads(response.text)
  if len(data)>0:
    price = data[0].get('current_price')
    print(price)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)