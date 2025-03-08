# src/etl.py
import pandas as pd
import os

def run_etl(share_prices_file: str, companies_file: str, output_dir: str):
    df_prices = pd.read_csv(share_prices_file)
    
    # Example columns: 'Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'
    # Adjust column names if needed
    # Parse date column
    df_prices['Date'] = pd.to_datetime(df_prices['Date'])
    
    # 2. (Optional) Filter for companies of interest or date ranges
    # my_tickers = ["AAPL", "MSFT", "GOOG", "TSLA", "AMZN"]
    # df_prices = df_prices[df_prices['Ticker'].isin(my_tickers)]
    
    # 3. Read the Companies file
    df_companies = pd.read_csv(companies_file)
    # Possibly rename columns or do merges if needed
    
    # 4. Merge data if relevant (for example, to add sector info)
    # df_merged = pd.merge(df_prices, df_companies, on="Ticker", how="left")
    
    # 5. Clean / transform the data
    # e.g., drop duplicates, handle missing values, etc.
    # df_merged.drop_duplicates(inplace=True)
    # df_merged.fillna(method="ffill", inplace=True)
    
    # For a minimal example, let's just keep df_prices
    df_clean = df_prices.dropna()
    
    # 6. Save processed data
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "share_prices_clean.csv")
    df_clean.to_csv(output_file, index=False)
    print(f"Processed data saved to: {output_file}")


if __name__ == "__main__":
    # Example usage:
    run_etl(
        share_prices_file="data/raw/share_prices.csv",
        companies_file="data/raw/companies.csv",
        output_dir="data/processed"
    )
