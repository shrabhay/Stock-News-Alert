import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import html
import os
os.system('clear')


def get_dates():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    day_before_yesterday = today - timedelta(days=2)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    day_before_yesterday_str = day_before_yesterday.strftime('%Y-%m-%d')

    return yesterday_str, day_before_yesterday_str


def stock_data(api_endpoint, api_parameters):
    yesterday_date, day_before_yesterday_date = get_dates()
    stock_response = requests.get(url=api_endpoint, params=api_parameters)
    stock_response.raise_for_status()
    stock_data_json = stock_response.json()
    yesterday_close = float(stock_data_json['Time Series (Daily)'][yesterday_date]['4. close'])
    day_before_yesterday_close = float(stock_data_json['Time Series (Daily)'][day_before_yesterday_date]['4. close'])

    return yesterday_close, day_before_yesterday_close


def news_data(api_endpoint, api_parameters):
    news_title = []
    news_description = []
    stock_news_response = requests.get(url=api_endpoint, params=api_parameters)
    stock_news_response.raise_for_status()
    stock_news_data = stock_news_response.json()
    news_articles = stock_news_data['articles'][:3]

    for news_article in news_articles:
        title = html.unescape(news_article['title'].replace('\n', '. '))
        news_title.append(title)
        description = html.unescape(news_article['description'].replace('\n', '. '))
        news_description.append(description)

    return news_title, news_description


def send_sms(account_sid, auth_token, sender, receiver, message_body):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=sender,
        to=receiver,
        body=message_body
    )

    whatsapp_message = client.messages.create(
        body=message_body,
        from_="whatsapp:+14155238886",
        to="whatsapp:+919871481094"
    )

    print(message.status)
    print(whatsapp_message.status)
