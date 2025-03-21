import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv


class ETL:
    def __init__(self, companies_file, shareprices_file, output_file, top_tickers=None):
        self.companies_file = companies_file
        self.shareprices_file = shareprices_file
        self.output_file = output_file
        self.top_tickers = top_tickers  
        self.df_companies = None
        self.df_shareprices = None
        self.df_merged = None

    def load_data(self):
        self.df_companies = pd.read_csv(self.companies_file, sep=";")
        self.df_shareprices = pd.read_csv(self.shareprices_file, sep=";")

    def filter_data(self):
        if self.top_tickers:
            self.df_companies = self.df_companies[self.df_companies['Ticker'].isin(self.top_tickers)]
            self.df_shareprices = self.df_shareprices[self.df_shareprices['Ticker'].isin(self.top_tickers)]
        if 'Dividend' in self.df_shareprices.columns:
            self.df_shareprices = self.df_shareprices.drop(columns=['Dividend'])
        if 'Date' in self.df_shareprices.columns:
            self.df_shareprices['Date'] = pd.to_datetime(self.df_shareprices['Date'])

    def merge_data(self):
        self.df_merged = pd.merge(
            self.df_shareprices, 
            self.df_companies, 
            on='Ticker', 
            how='left', 
            suffixes=('_price', '_company')
        )

    def save_data(self):
        if self.df_merged is not None:
            self.df_merged.to_csv(self.output_file, index=False)
            print(f"Merged DataFrame saved to {self.output_file}")
        else:
            raise Exception("Merged data is not available. Please run merge_data() first.")

    def run(self):
        self.load_data()
        self.filter_data()
        self.merge_data()
        self.save_data()


if __name__ == '__main__':
    load_dotenv()

    # Get the base directory of the project
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Define file paths relative to the project folder
    companies_file = os.path.join(BASE_DIR, 'data/raw/us-companies.csv')
    shareprices_file = os.path.join(BASE_DIR, 'data/raw/us-shareprices-daily.csv')
    output_file = os.path.join(BASE_DIR, 'data/processed/output.csv')

    # Run ETL process
    etl = ETL(companies_file, shareprices_file, output_file)
    etl.run()
