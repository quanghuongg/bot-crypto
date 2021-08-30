import requests
import schedule
import time

apiToken = "1963172772:AAH4S85fJz_IuToeu6mBhMAyrC16PqxwGkE"
chatId = "-544454140"
text = "Pet your gotchi "


def job():
    urlString = f'https://api.telegram.org/bot{apiToken}/sendMessage?chat_id={chatId}&text={text}'
    requests.get(urlString)


schedule.every().day.at("21:48").do(job)
schedule.every().day.at("09:48").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
