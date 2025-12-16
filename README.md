# News Sentiment Analyzer for Stock Predictions

## What it does
Collects financial news articles for major stocks, analyzes sentiment, and correlates with price movements to predict next-day stock direction.

## Data Science concepts
- Natural Language Processing (NLP)
- Sentiment analysis (VADER)
- Time series analysis
- Correlation analysis
- Machine Learning (classification)
- Feature engineering
- Data visualization

## Tech stack

### Data Collection & Storage
- News API - Financial news articles
- yfinance - Stock price data
- SQLite - Database
- pandas - Data manipulation
- requests - API calls

### NLP & Sentiment
- VADER (vaderSentiment) - Sentiment analysis
- NLTK - Text processing
- TextBlob - Alternative sentiment (optional)

### Machine Learning
- scikit-learn - ML models and evaluation
- XGBoost - Gradient boosting (optional)
- NumPy - Numerical operations
- scipy - Statistical analysis

### Visualization & Dashboard
- Streamlit - Web dashboard
- Plotly - Interactive charts
- Matplotlib - Static plots (optional)

### Automation & Deployment
- schedule - Task automation
- python-dotenv - Environment variables
- joblib - Model persistence
- Git/GitHub - Version control
- Streamlit Cloud - Free hosting

## Project phases

### Week 1: Data Collection (Dec 16-22)
- Set up News API and collect financial news
- Build multi-stock news scraper
- Set up SQLite database
- Fetch historical stock prices with yfinance
- Create unified dataset

### Week 2: Sentiment Analysis (Dec 23-29)
- Learn NLP and VADER sentiment
- Implement text preprocessing
- Analyze news sentiment by stock
- Correlation analysis
- Feature engineering

### Week 3: Machine Learning (Dec 30 - Jan 5)
- Prepare data for ML
- Build baseline and advanced models
- Model evaluation and tuning
- Build Streamlit dashboard

### Week 4: Deployment (Jan 6-12)
- Automation setup
- Dashboard polish
- Testing and deployment

## Author
tanay-jagadeesh
