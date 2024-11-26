# Stock News Alert
## Description
This project provides a stock news alert service that sends SMS notifications whenever a stock's price changes, along with the latest news about the respective company. The service checks the stock price change between two consecutive days and sends an SMS with the change percentage and the top 3 related news headlines.

---

## Project Files

The project contains the following two Python files:

1. `functions.py`: Contains utility functions for fetching stock data, news articles, and sending SMS using the Twilio API.
2. `stock_news_alert.py`: Main script that integrates the stock and news data functions and sends the SMS alert.

---

## API Keys and Setup

To run this project, you'll need to obtain API keys for the following services:

### 1. Alpha Vantage (Stock Data API)

Alpha Vantage provides free stock market data. You'll need to get an API key from them to access stock data.

#### Steps to get the API key:
- Go to [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
- Sign up for a free account if you don't have one.
- After logging in, you'll be able to generate an API key from your account dashboard.

Once you have the API key, add it to the `STOCK_API_KEY` variable in `stock_news_alert.py`.

### 2. NewsAPI (News Data API)

NewsAPI provides news articles from a wide range of sources. You'll need to get an API key from them to access news data.

#### Steps to get the API key:
- Go to [NewsAPI](https://newsapi.org/).
- Sign up for a free account.
- After logging in, you'll be able to generate an API key from your account dashboard.

Once you have the API key, add it to the `NEWS_API_KEY` variable in `stock_news_alert.py`.

### 3. Twilio (SMS API)

Twilio provides an API for sending SMS messages. You'll need to create a Twilio account and obtain an account SID, authentication token, and phone numbers.

#### Steps to get the Twilio API credentials:
- Go to [Twilio](https://www.twilio.com/).
- Sign up for a free account.
- After logging in, you'll be able to find your Account SID and Auth Token on the [Twilio Console](https://www.twilio.com/console).
- You can get a Twilio phone number from the console as well. You’ll need this for the `SMS_SENDER` variable.
- You can use your personal phone number for the `SMS_RECIPIENT` variable.

### Setting Up the Project

1. Clone the repository to your local machine:
   ```commandline
   git clone https://github.com/shrabhay/Stock-News-Alert.git
   cd Stock-News-Alert
   ```

2. Install the required dependencies:
    ```commandline
    pip install requests twilio
    ```

3. Configure the API keys:
   * Replace `<YOUR_STOCK_API_KEY>` with your Alpha Vantage API key in `stock_news_alert.py`.
   * Replace `<YOUR_NEWS_API_KEY>` with your NewsAPI API key in `stock_news_alert.py`.
   * Replace `<YOUR_TWILLIO_SMS_ACCOUNT_SID>`, `<YOUR_TWILLIO_SMS_AUTH_TOKEN>`, `<SENDER_NUMBER>`, and 
     `<RECEIVER_NUMBER>` with your Twilio API credentials and phone numbers.

4. Run the script:
    ```commandline
    python3 stock_news_alert.py
    ```

    The script will check for stock price changes and send SMS notifications with the top 3 news headlines related to the specified company.

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.
