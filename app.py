# **************** IMPORT PACKAGES ********************
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from datetime import datetime
import os
import yfinance as yf
import warnings
import requests
from dotenv import load_dotenv  # Import dotenv for environment variables
# importing modules from models.py
from models import run_arima, run_lstm, run_lr

warnings.filterwarnings("ignore")

# ***************** FLASK *****************************
app = Flask(__name__)

# Load environment variables
load_dotenv()  # Take environment variables from .env file

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "815d56be9aa94592ad061cce7dd571e1")  # Use env variable with fallback
NEWS_API_URL = 'https://newsapi.org/v2/everything'
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "GVTB99LP1GHVJCVG")

# ****************** ROUTES ****************************
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index.html')
def stock_prediction():
    return render_template('index.html')

@app.route('/currency.html')
def currency_converter():
    return render_template('currency.html')

@app.route('/news.html')
def news():
    return render_template('news.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/service.html')
def services():
    return render_template('service.html')

@app.route('/blog')
def blogs():
    return render_template('blog.html')

@app.route('/contact')
def contactus():
    return render_template('contact.html')

@app.route('/feature')
def features():
    return render_template('feature.html')

@app.route('/team')
def team():
    return render_template('team.html')

# ***************** HELPER FUNCTIONS ***************************
def get_historical(quote):
    try:
        end = datetime.now()
        start = datetime(end.year - 2, end.month, end.day)
        df = yf.download(quote, start=start, end=end)
        if not df.empty:
            df = df.reset_index()
            if 'Date' in df.columns:
                df['Date'] = pd.to_datetime(df['Date'])  
                df.set_index('Date', inplace=True)
            else:
                raise ValueError("'Date' column not found in the downloaded data.")
            df.to_csv(f'{quote}.csv')
        else:
            from alpha_vantage.timeseries import TimeSeries
            ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
            data, _ = ts.get_daily_adjusted(symbol=f'NSE:{quote}', outputsize='full')
            data = data.head(503).iloc[::-1].reset_index()
            df = data[['date', '1. open', '2. high', '3. low', '4. close', '5. adjusted close', '6. volume']]
            df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
            df.to_csv(f'{quote}.csv', index=False)
        return df
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return None

@app.route('/get_news', methods=['POST'])
def get_news():
    symbol = request.form.get('symbol')
    
    if not symbol:
        return jsonify({'error': 'No stock symbol provided'}), 400

    query = f"{symbol} business"
    
    try:
        response = requests.get(NEWS_API_URL, params={
            'q': query,
            'apiKey': NEWS_API_KEY,
            'sortBy': 'publishedAt'
        })
        
        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch news'}), response.status_code
        
        data = response.json()

        if data['status'] == 'ok':
            return jsonify(data['articles'])
        else:
            return jsonify({'error': 'Error fetching news from the API'}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stock_details', methods=['POST'])
def stock_details():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol'].upper()
        if not stock_symbol.endswith('.NS'):
            stock_symbol += '.NS'
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info or {}

        # Fetching additional company details
        stock_name = stock_info.get('longName', 'N/A')
        sector = stock_info.get('sector', 'N/A')
        industry = stock_info.get('industry', 'N/A')
        description = stock_info.get('longBusinessSummary', 'N/A')

        # Fetching stock splits
        stock_splits = stock.splits

        # Fetching dividends
        dividends = stock.dividends

        # Fetching financial statements
        income_statement = stock.financials
        balance_sheet = stock.balance_sheet
        cash_flow = stock.cashflow
        market_cap = stock_info.get('marketCap', 'N/A')
        pe_ratio = stock_info.get('trailingPE', 'N/A')
        pb_ratio = stock_info.get('priceToBook', 'N/A')
        dividend_yield = stock_info.get('dividendYield', 'N/A')
        high_price = stock_info.get('dayHigh', 'N/A')
        low_price = stock_info.get('dayLow', 'N/A')
        roe = stock_info.get('returnOnEquity', 'N/A')
        fifty_two_week_high = stock_info.get('fiftyTwoWeekHigh', 'N/A')
        fifty_two_week_low = stock_info.get('fiftyTwoWeekLow', 'N/A')
        no_of_shares = stock_info.get('sharesOutstanding', 'N/A')
        enterprise_value = stock_info.get('enterpriseValue', 'N/A')
        debt = stock_info.get('totalDebt', 'N/A')

        try:
            df = get_historical(stock_symbol)
            if df is None or df.empty:
                raise ValueError("Failed to retrieve data or data is empty.")

            df["Code"] = stock_symbol

            latest_data = df.iloc[-1]
            todays_open = latest_data['Open']
            todays_close = latest_data['Close']
            todays_adj_close = latest_data['Adj Close']
            todays_volume = latest_data['Volume']
            todays_high = latest_data['High']
            todays_low = latest_data['Low']

            ARIMA_pred, error_ARIMA = run_arima(df)
            LSTM_pred, error_LSTM = run_lstm(df)
            LR_pred, error_LR = run_lr(df)

            return render_template(
                'stock_details.html', 
                stock_symbol=stock_symbol, 
                stock_name=stock_name, 
                sector=sector, 
                industry=industry, 
                description=description,
                stock_splits=stock_splits.to_dict() if not stock_splits.empty else 'N/A',
                dividends=dividends.to_dict() if not dividends.empty else 'N/A',
                income_statement=income_statement.to_dict() if not income_statement.empty else 'N/A',
                balance_sheet=balance_sheet.to_dict() if not balance_sheet.empty else 'N/A',
                cash_flow=cash_flow.to_dict() if not cash_flow.empty else 'N/A',
                market_cap=market_cap, 
                pe_ratio=pe_ratio, 
                pb_ratio=pb_ratio, 
                dividend_yield=dividend_yield,
                roe=roe, 
                fifty_two_week_high=fifty_two_week_high, 
                fifty_two_week_low=fifty_two_week_low, 
                no_of_shares=no_of_shares, 
                enterprise_value=enterprise_value, 
                debt=debt,
                ARIMA_pred=ARIMA_pred, 
                LSTM_pred=LSTM_pred, 
                LR_pred=LR_pred)
        except Exception as e:
            return render_template('error.html', error_message=str(e))

# ******************* MAIN *******************************
if __name__ == "__main__":
    app.run(debug=True)
