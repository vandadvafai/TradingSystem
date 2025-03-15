import os
from dotenv import load_dotenv 
import simfin as sf
import pandas as pd
import logging

### I will be using the SIMFIN API in my program. I want to be able to just extract the tickers and dates
### for the stock prices to be using them in the function. How do I do that?

# Load environment variables
load_dotenv()

class api_wrapper:
    def __init__(self):
        self.api_key = os.getenv("SIMFIN_API_KEY")
        
        if not self.api_key:
            raise ValueError("API Key not found. Please set SIMFIN_API_KEY in .env file.")
        sf.set_api_key(self.api_key)
        sf.set_data_dir('~/simfin_data/')
        logging.basicConfig(level=logging.INFO)

    def get_share_prices(self, ticker: str, start: str, end: str):
        try:
            prices_df = sf.load_shareprices(variant='daily')
            # Reset index to make filtering easier
            prices_df = prices_df.reset_index()
            prices_df = prices_df[
                (prices_df['Ticker'] == ticker) & 
                (prices_df['Date'] >= start) & 
                (prices_df['Date'] <= end)
            ]

            logging.info(f"Successfully retrieved share price data for {ticker}.")
            return prices_df
        except Exception as e:
            logging.error(f"Error fetching share prices: {e}")
            return None


    def get_financial_statements(self, ticker: str, start: str, end: str):
        try:
            financials_df = sf.load_income(variant='quarterly')
            financials_df = financials_df.reset_index()
            financials_df = financials_df[
                (financials_df['Ticker'] == ticker) & 
                (financials_df['Report Date'] >= start) & 
                (financials_df['Report Date'] <= end)
            ]

            logging.info(f"Successfully retrieved all income statements for {ticker}.")
            return financials_df
        except Exception as e:
            logging.error(f"Error fetching financial statements: {e}")
            return None

# Example Usage
if __name__ == "__main__":
    simfin = api_wrapper()
    
    # Fetch share prices
    stock_data = simfin.get_share_prices("AAPL", "2023-01-01", "2023-12-31")
    print(stock_data.head() if stock_data is not None else "No data available.")

    # Fetch financial statements
    financial_data = simfin.get_financial_statements("AAPL", "2023-01-01", "2023-12-31")
    print(financial_data.head() if financial_data is not None else "No data available.")