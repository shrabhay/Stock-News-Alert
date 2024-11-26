from functions import stock_data, news_data, send_sms
import os
os.system('clear')

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = 'CVGAHX90AWVCRQOA'
STOCK_API_FUNCTION = 'TIME_SERIES_DAILY'
STOCK_API_PARAMETERS = {
    'function': STOCK_API_FUNCTION,
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}

NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = '7324bf0a200441fd9276ba15e53a8360'
NEWS_API_PARAMETERS = {
    'q': COMPANY_NAME,
    'sortBy': 'publishedAt',
    'language': 'en',
    'searchIn': 'title',
    'apiKey': NEWS_API_KEY
}

SMS_ACCOUNT_SID = 'AC47fe4a9bfeac7e5c6a51cd0ff4198f87'
SMS_AUTH_TOKEN = 'aae220661ef58be6b0d2be5960cd7775'
SMS_SENDER = '+14159693474'
SMS_RECIPIENT = '+919871481094'

# stock_close_yesterday = 200
# stock_close_day_before_yesterday = 250
stock_close_yesterday, stock_close_day_before_yesterday = stock_data(
    api_endpoint=STOCK_API_ENDPOINT,
    api_parameters=STOCK_API_PARAMETERS
)
# print(stock_close_yesterday, stock_close_day_before_yesterday)

stock_price_change = round((((stock_close_yesterday - stock_close_day_before_yesterday) / stock_close_yesterday)
                            * 100), 2)
# print(stock_price_change)

if abs(stock_price_change) > 0:
    news_article_titles, news_article_descriptions = news_data(
        api_endpoint=NEWS_API_ENDPOINT,
        api_parameters=NEWS_API_PARAMETERS
    )

    for i in range(3):
        change_symbol = '🔺' if stock_price_change > 0 else '🔻'
        sms_body = (f"{STOCK}: {change_symbol} {abs(stock_price_change)}%\nHeadline: {news_article_titles[i]}\nBrief:"
                    f" {news_article_descriptions[i]}")

        send_sms(
            account_sid=SMS_ACCOUNT_SID,
            auth_token=SMS_AUTH_TOKEN,
            sender=SMS_SENDER,
            receiver=SMS_RECIPIENT,
            message_body=sms_body
        )
