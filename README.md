Automated Daily Trading System

Project Overview

This project is an Automated Daily Trading System developed using Python. The system comprises two primary components:

Data Analytics Module: A machine learning (ML) model that forecasts market movements based on historical stock prices.

Web-Based Application: A multi-page Streamlit application that allows users to visualize market data, interact with the predictive model, and execute trading strategies.

The trading system integrates financial data from SimFin, a financial data provider, to analyze historical trends and predict future stock price movements.

Team Members

[Your Team Member Names Here]

Project Structure

The repository is organized as follows:

TRADINGSYSTEM/
│── app_pages/
│   ├── go_live.py               # Streamlit page for real-time stock tracking
│   ├── home.py                  # Streamlit homepage
│   ├── trading_strategy.py       # Streamlit page for visualizing strategies
│
│── data/
│   ├── processed/
│   │   ├── output.csv            # Processed dataset
│   ├── raw/
│   │   ├── us-companies.csv      # List of US companies
│   │   ├── us-shareprices-daily.csv # Daily share prices
│
│── src/
│   ├── api_wrapper.py            # API wrapper for SimFin
│   ├── ETL.py                    # Extract, Transform, Load process
│   ├── model.py                  # ML model for stock prediction
│   ├── trading_strat.py          # Trading strategy implementation
│
│── .env                          # Environment variables (API keys, etc.)
│── .gitignore                    # Files to be ignored in version control
│── README.md                     # Project documentation
│── scaler.pkl                     # Scaler for data normalization
│── stock_price_predictor.pkl      # Trained ML model
│── streamlit_app.py               # Main Streamlit app file

Explanation of Each File

1. Streamlit App Pages (app_pages/)

home.py: Displays an overview of the trading system and its functionalities.

go_live.py: Allows users to select stocks, retrieve real-time data, and display ML predictions.

trading_strategy.py: Visualizes different trading strategies based on ML model outputs.

2. Data Processing (data/)

raw/us-companies.csv: Contains details of US companies.

raw/us-shareprices-daily.csv: Historical share prices of selected companies.

processed/output.csv: Cleaned dataset after ETL processing.

3. Source Code (src/)

api_wrapper.py: Python wrapper to retrieve financial data from SimFin.

ETL.py: Extracts raw financial data, transforms it, and loads it into the system for analysis.

model.py: Builds and trains an ML model to predict stock market movements.

trading_strat.py: Implements different trading strategies based on the ML model’s output.

4. Other Files

.env: Stores API keys and other environment variables (not included in version control).

scaler.pkl: Pre-trained scaler used to normalize data before predictions.

stock_price_predictor.pkl: The trained ML model used for real-time predictions.

streamlit_app.py: Main script to run the Streamlit web application.

How to Run the Project

Step 1: Install Dependencies

Ensure you have Python 3.8+ installed, then install the required libraries:

pip install -r requirements.txt

Step 2: Run the ETL Pipeline

Before using the Streamlit application, process the raw data by running:

python src/ETL.py

Step 3: Train the Machine Learning Model

Run the following command to train and save the model:

python src/model.py

Step 4: Start the Streamlit Web Application

Once the data is processed and the model is trained, launch the Streamlit app:

streamlit run streamlit_app.py

Key Features

✅ Real-time market analysis using financial data from SimFin
✅ Predictive analytics leveraging ML to forecast stock movements
✅ User-friendly interface built with Streamlit
✅ Automated trading strategies based on model outputs

Future Enhancements

Implement backtesting for trading strategies.

Deploy the system on a cloud platform for remote access.

Enhance the ML model with deep learning techniques.

