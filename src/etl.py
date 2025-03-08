import os
import pandas as pd
import simfin as sf
from dotenv import load_dotenv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle
import numpy as np

class ETL:
    def __init__(self, companies_file, shareprices_file, output_file, top_tickers=None):
        self.companies_file = companies_file
        self.shareprices_file = shareprices_file
        self.output_file = output_file
        self.top_tickers = top_tickers or ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA', 'META']
        self.df_companies = None
        self.df_shareprices = None
        self.df_merged = None

    # Load companies and share prices data from CSV files.
    def load_data(self):
        self.df_companies = pd.read_csv(self.companies_file, sep=";")
        self.df_shareprices = pd.read_csv(self.shareprices_file, sep=";")
        print("Data loaded.")

    # Filter for top tickers and perform necessary cleaning.
    def filter_data(self):
        # Filter for the top tickers
        self.df_companies = self.df_companies[self.df_companies['Ticker'].isin(self.top_tickers)]
        self.df_shareprices = self.df_shareprices[self.df_shareprices['Ticker'].isin(self.top_tickers)]
        
        # Remove the 'Dividend' column if it exists
        if 'Dividend' in self.df_shareprices.columns:
            self.df_shareprices = self.df_shareprices.drop(columns=['Dividend'])
        
        # Convert the Date column to datetime format if it exists
        if 'Date' in self.df_shareprices.columns:
            self.df_shareprices['Date'] = pd.to_datetime(self.df_shareprices['Date'])
        
        print("Data filtered and cleaned.")

    # Merge the share prices data with the companies data.
    def merge_data(self):
        self.df_merged = pd.merge(
            self.df_shareprices, 
            self.df_companies, 
            on='Ticker', 
            how='left', 
            suffixes=('_price', '_company')
        )
        print("Data merged.")

    # Save the merged DataFrame to a CSV file.
    def save_data(self):
        if self.df_merged is not None:
            self.df_merged.to_csv(self.output_file, index=False)
            print(f"Merged DataFrame saved to {self.output_file}")
        else:
            print("Merged data is not available. Please run merge_data() first.")

    # Execute the full ETL process.
    def run(self):
        self.load_data()
        self.filter_data()
        self.merge_data()
        self.save_data()


if __name__ == '__main__':
    # Optionally load environment variables
    load_dotenv()
    
    companies_file = '/Users/vandad/Desktop/TradingSystem/data/raw/us-companies.csv'
    shareprices_file = '/Users/vandad/Desktop/TradingSystem/data/raw/us-shareprices-daily.csv'
    output_file = '/Users/vandad/Desktop/TradingSystem/data/processed/output.csv'

    etl = ETL(companies_file, shareprices_file, output_file)
    etl.run()
