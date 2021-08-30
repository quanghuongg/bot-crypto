from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler
import requests
from bs4 import BeautifulSoup
import json


# 283610bf-d405-44cf-90f4-07c064c06f70

def get_news():
    res = requests.get("https://zingnews.vn/cong-nghe.html")
    soup = BeautifulSoup(res.text, 'html.parser')
    mydivs = soup.find_all("p", {"class": "article-title"})
    list = []
    for new in mydivs:
        list.append("https://zingnews.vn" + new.a.get('href'))
    return list


def get_price(coin, update: Update, context: CallbackContext):
    coin = coin.replace("/", "")
    url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&symbols={coin}'
    data = json.loads(requests.get(url, verify=False, timeout=10).text)
    print(data)
    if len(data) > 0:
        price = data[0].get('current_price')
        coin = coin.upper()
        update.message.reply_text(f'{coin}: {price} $')
    else:
        update.message.reply_text(f'Not found')


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def news(update: Update, context: CallbackContext) -> None:
    data = get_news()
    data = data[0:5]
    for new in data:
        update.message.reply_text(f'{new}')


def doAction(cmd, update, context):
    switcher = {
        "/news": lambda: news(update, context),
        "/hello": lambda: hello(update, context),
    }
    func = switcher.get(cmd, lambda: get_price(cmd, update, context))
    func()


def reply(update, context):
    user_input = update.message.text
    doAction(user_input, update, context)


updater = Updater('1963172772:AAH4S85fJz_IuToeu6mBhMAyrC16PqxwGkE')
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, reply))
updater.start_polling()
updater.idle()
