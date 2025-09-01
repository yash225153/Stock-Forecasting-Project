# 📈 Stock Forecasting Project

A comprehensive web application for stock market analysis and prediction using machine learning algorithms. This project provides real-time stock data analysis, price predictions, currency conversion, and financial news aggregation.

![Home Page](Project%20Images/home1.png)

## 🚀 Features

### 📊 Stock Price Prediction
- **ARIMA Model**: Time series forecasting using AutoRegressive Integrated Moving Average
- **LSTM Neural Network**: Deep learning approach for sequential data prediction
- **Linear Regression**: Statistical model for trend analysis
- **Real-time Data**: Fetches live stock data from Yahoo Finance API

### 💱 Currency Converter
- Real-time currency exchange rates
- Support for multiple international currencies
- Clean and intuitive interface

![Currency Converter](Project%20Images/Currency_Converter.png)

### 📰 Stock News
- Latest financial news and market updates
- News aggregation from multiple sources
- Relevant stock market information

![Stock News](Project%20Images/stock%20news.png)

### 📈 Detailed Stock Analysis
- Comprehensive stock information including:
  - Market capitalization
  - P/E ratio, P/B ratio
  - 52-week high/low
  - Dividend yield
  - Financial statements
  - Stock splits and dividends history

![Stock Details 1](Project%20Images/stock_details1.png)
![Stock Details 2](Project%20Images/stock_details2.png)
![Stock Details 3](Project%20Images/stock_details3.png)

## 🛠️ Technology Stack

### Backend
- **Python 3.10+**
- **Flask** - Web framework
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **yfinance** - Yahoo Finance API wrapper
- **scikit-learn** - Machine learning library
- **TensorFlow/Keras** - Deep learning framework
- **statsmodels** - Statistical modeling (ARIMA)
- **matplotlib** - Data visualization

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling and layout
- **JavaScript** - Interactive functionality
- **Bootstrap** - Responsive design framework

### APIs
- **Yahoo Finance API** - Stock data
- **News API** - Financial news
- **Alpha Vantage API** - Alternative stock data source

## 📁 Project Structure

```
Stock-Forecasting-Project/
├── app.py                 # Main Flask application
├── models.py              # Machine learning models (ARIMA, LSTM, LR)
├── templates/             # HTML templates
│   ├── home.html         # Landing page
│   ├── index.html        # Stock prediction page
│   ├── stock_details.html # Detailed stock analysis
│   ├── currency.html     # Currency converter
│   ├── news.html         # Stock news
│   ├── about.html        # About page
│   └── ...
├── static/               # Static assets
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   ├── images/          # Generated charts and images
│   └── ...
├── Project Images/       # Application screenshots
└── requirements.txt      # Python dependencies
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yash225153/Stock-Forecasting-Project.git
cd Stock-Forecasting-Project
```

### Step 2: Install Dependencies
```bash
pip install flask pandas numpy yfinance python-dotenv requests alpha-vantage scikit-learn tensorflow matplotlib statsmodels
```

### Step 3: Set Up Environment Variables (Optional)
Create a `.env` file in the project root:
```env
NEWS_API_KEY=your_news_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
```

### Step 4: Run the Application
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## 🎯 Usage

### Stock Prediction
1. Navigate to the stock prediction page
2. Enter a stock symbol (e.g., RELIANCE, TCS, INFY)
3. View predictions from three different models
4. Analyze generated charts and accuracy metrics

![Stock Search](Project%20Images/stock_search.png)

### Currency Conversion
1. Go to the currency converter page
2. Select source and target currencies
3. Enter the amount to convert
4. Get real-time exchange rates

### Stock News
1. Visit the news section
2. Browse latest financial news
3. Stay updated with market trends

## 🤖 Machine Learning Models

### 1. ARIMA (AutoRegressive Integrated Moving Average)
- **Purpose**: Time series forecasting
- **Best for**: Short to medium-term predictions
- **Parameters**: (6,1,0) configuration
- **Output**: Price predictions with trend analysis

### 2. LSTM (Long Short-Term Memory)
- **Purpose**: Deep learning for sequential data
- **Architecture**: 4 LSTM layers with dropout
- **Training**: 25 epochs with batch size 32
- **Best for**: Capturing long-term dependencies

### 3. Linear Regression
- **Purpose**: Statistical trend analysis
- **Features**: Historical price data
- **Best for**: Linear trend identification
- **Output**: 7-day ahead predictions

## 📊 Supported Stock Markets
- **NSE (National Stock Exchange)** - Primary focus
- **Indian stocks** with .NS suffix
- Examples: RELIANCE.NS, TCS.NS, INFY.NS, HDFCBANK.NS

## 🖼️ Screenshots

### About Page
![About](Project%20Images/about.png)

### Services
![Services](Project%20Images/services.png)

### Blog
![Blog](Project%20Images/blog.png)

### Contact
![Contact](Project%20Images/contact.png)

## 🔮 Future Enhancements
- [ ] Support for international stock markets
- [ ] Portfolio management features
- [ ] Real-time alerts and notifications
- [ ] Mobile application
- [ ] Advanced technical indicators
- [ ] Sentiment analysis from news
- [ ] User authentication and personalization

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## 👨‍💻 Author
**Yash** - [yash225153](https://github.com/yash225153)

## 🙏 Acknowledgments
- Template by [HTML Codex](https://htmlcodex.com)
- Yahoo Finance for stock data
- News API for financial news
- TensorFlow and scikit-learn communities

## 📞 Support
If you have any questions or issues, please open an issue on GitHub or contact the author.

---
⭐ **Star this repository if you found it helpful!**
