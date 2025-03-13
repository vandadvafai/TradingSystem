import pandas as pd
import joblib
import logging
from api_wrapper import api_wrapper

class TradingStrategy:
    def __init__(self, model_path='stock_price_predictor.pkl', scaler_path='scaler.pkl', initial_cash=1000):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.cash = initial_cash
        self.shares = 0
        self.trade_log = []

    def apply_strategy(self, df):
        features = ['Open', 'High', 'Low', 'Close', 'Volume']
        X = df[features]
        X_scaled = self.scaler.transform(X)

        df['Prediction'] = self.model.predict(X_scaled)

        for index, row in df.iterrows():
            price = row['Close']
            if row['Prediction'] == 1:  # Buy signal
                shares_to_buy = self.cash // price
                self.shares += shares_to_buy
                self.cash -= shares_to_buy * price
                self.trade_log.append(f"BUY {shares_to_buy} shares at {price}")
            elif row['Prediction'] == 0 and self.shares > 0:  # Sell signal
                self.cash += self.shares * price
                self.trade_log.append(f"SELL {self.shares} shares at {price}")
                self.shares = 0
        
        return self.cash, self.shares

# Example usage
if __name__ == "__main__":
    api = api_wrapper()
    stock_data = api.get_share_prices("AAPL", "2023-01-01", "2023-12-31")

    if stock_data is not None and not stock_data.empty:
        strategy = TradingStrategy()
        final_cash, final_shares = strategy.apply_strategy(stock_data)
        print("Final Portfolio Value:", final_cash + final_shares * stock_data.iloc[-1]['Close'])
    else:
        logging.error("No stock data available for trading.")
